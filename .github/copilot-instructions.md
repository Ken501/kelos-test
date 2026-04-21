# Automated PR Review Instructions

1. When doing a PR review on both a Draft PR or a PR in Ready state leave a comment on in the conversations tab of the PR with just the "ready" word and nothing else if you don't find any issues. If there are issues then leave a comment in the conversations tab with just the "comment" word and nothing else. Both comments will go in the conversations tab of the PR. DO NOT post a comment on the file being reviewed. ONLY POST COMMENTS ON THE PR CONVERSATONS TAB.

If you do something similar to this then it is WRONG. Add a regular PR comment, holy shit.:

```json
{
  "comment_content": "ready",
  "comment_type": "custom",
  "corrected_text": "",
  "end_line": 1,
  "file_location": "main.py",
  "fixed": false,
  "guideline_id": "1000000",
  "original_text": "",
  "severity": "nit",
  "start_line": 1
}
```
