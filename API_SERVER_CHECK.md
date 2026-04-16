# Kubernetes API Server Connectivity Check

**Date:** 2026-04-16
**Service Account:** `system:serviceaccount:kelos-system:bedrock-agent-sa`
**Namespace:** `kelos-system`
**API Server:** `https://172.20.0.1:443`

## Summary

All core K8s API server endpoints are reachable and healthy. The agent's service account can successfully authenticate and query cluster metadata.

| Endpoint | HTTP Status | Result |
|----------|-------------|--------|
| `/version` | 200 | OK |
| `/healthz` | 200 | ok |
| `/livez` | 200 | ok |
| `/readyz` | 200 | ok |
| `/apis` | 200 | OK |
| `/api/v1` | 200 | OK |

## Detailed Results

### 1. API Server Version (`/version`)

```json
{
  "major": "1",
  "minor": "32",
  "gitVersion": "v1.32.12-eks-f69f56f",
  "gitCommit": "2bb21951f0a44ab4d4989306d161ffc8e8ff8cb8",
  "gitTreeState": "clean",
  "buildDate": "2026-02-27T11:18:54Z",
  "goVersion": "go1.24.13",
  "compiler": "gc",
  "platform": "linux/amd64"
}
```

### 2. Health Endpoints

- **`/healthz`** — `ok`
- **`/livez`** — `ok`
- **`/readyz`** — `ok`

### 3. API Discovery (`/apis`)

The API server returned a valid `APIGroupList` including standard groups: `apiregistration.k8s.io`, `apps`, `events.k8s.io`, `authentication.k8s.io`, and others.

### 4. Core API Resources (`/api/v1`)

The API server returned a valid `APIResourceList` for the `v1` group, listing core resources such as `bindings`, `componentstatuses`, `configmaps`, and more.

### 5. RBAC Note — Pod Listing

Listing pods in the `kelos-system` namespace returned **403 Forbidden**, which is expected given the service account's RBAC permissions:

```
pods is forbidden: User "system:serviceaccount:kelos-system:bedrock-agent-sa" cannot list resource "pods" in API group "" in the namespace "kelos-system"
```

This confirms RBAC is enforced correctly. The service account can authenticate and reach the API server but does not have broad resource-listing privileges.

## Curl Commands Used

```bash
APISERVER="https://${KUBERNETES_SERVICE_HOST}:${KUBERNETES_SERVICE_PORT}"
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
CACERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt

# Version
curl -s --cacert "$CACERT" -H "Authorization: Bearer $TOKEN" "$APISERVER/version"

# Health checks
curl -s --cacert "$CACERT" -H "Authorization: Bearer $TOKEN" "$APISERVER/healthz"
curl -s --cacert "$CACERT" -H "Authorization: Bearer $TOKEN" "$APISERVER/livez"
curl -s --cacert "$CACERT" -H "Authorization: Bearer $TOKEN" "$APISERVER/readyz"

# API discovery
curl -s --cacert "$CACERT" -H "Authorization: Bearer $TOKEN" "$APISERVER/apis"
curl -s --cacert "$CACERT" -H "Authorization: Bearer $TOKEN" "$APISERVER/api/v1"

# Pod listing (RBAC test)
curl -s --cacert "$CACERT" -H "Authorization: Bearer $TOKEN" \
  "$APISERVER/api/v1/namespaces/kelos-system/pods"
```

## Conclusion

The agent can successfully communicate with the Kubernetes API server. Authentication via the mounted service account token works correctly, and the API server is healthy on all health endpoints.
