# Kubernetes API Server Connectivity Check

**Date:** 2026-04-17
**Namespace:** kelos-system
**API Server:** https://172.20.0.1:443
**Service Account:** system:serviceaccount:kelos-system:bedrock-agent-sa

## Results Summary

| Check | Result |
|---|---|
| API Server Reachable | YES |
| HTTP Status | 200 |
| livez | ok |
| readyz | ok |
| Response Time | ~6ms |
| Authentication | Valid (Bearer token accepted) |

## 1. API Server Version

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

**Cluster:** EKS, Kubernetes v1.32.12

## 2. Health Checks

**livez endpoint** (`/livez`):
```
ok
```

**readyz endpoint** (`/readyz`):
```
ok
```

Both health endpoints confirm the API server is live and ready to serve requests.

## 3. API Groups Discovery

The `/apis` endpoint returned a valid `APIGroupList` including core groups:
- `apiregistration.k8s.io/v1`
- `apps/v1`
- `events.k8s.io/v1`
- `authentication.k8s.io/v1`
- `authorization.k8s.io/v1`
- `autoscaling/v2`, `autoscaling/v1`

API discovery is functioning correctly.

## 4. RBAC / Authorization Check

Listing pods in the `kelos-system` namespace returned **403 Forbidden**:

```
pods is forbidden: User "system:serviceaccount:kelos-system:bedrock-agent-sa"
cannot list resource "pods" in API group "" in the namespace "kelos-system"
```

This is expected behavior -- the service account authenticates successfully but does not have RBAC permissions to list pods. This confirms that authentication works and RBAC is properly enforcing least-privilege access.

## 5. Response Performance

```
HTTP Status: 200
Time Total: 0.006479s
```

The API server responded in ~6ms, indicating healthy in-cluster networking.

## Conclusion

The agent can successfully communicate with the Kubernetes API server. Authentication via the mounted service account token is working, the API server is healthy (livez/readyz both ok), and RBAC is correctly scoped.
