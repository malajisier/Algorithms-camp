# 遍历
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)


# 切片，不推荐
class Solution1:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]