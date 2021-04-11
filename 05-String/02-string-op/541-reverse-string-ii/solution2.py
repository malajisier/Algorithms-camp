class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l, mid, r = 0, k, 2 * k
        res = ''

        while len(res) < len(s):
            res += s[l : mid][::-1] + s[mid : r]
            l, mid, r = l + 2 * k, mid + 2 * k, r + 2 * k;

        return res 
        