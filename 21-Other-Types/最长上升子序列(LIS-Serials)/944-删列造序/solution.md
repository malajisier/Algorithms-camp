```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        counts = 0
        cols, rows = len(A[0]), len(A)
        for i in range(cols):
            for j in range(rows - 1):
                if A[j][i] > A[j + 1][i]:
                    counts += 1
                    break
        return counts
```

