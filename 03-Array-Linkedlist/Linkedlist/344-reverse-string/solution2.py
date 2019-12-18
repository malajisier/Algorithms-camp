class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """'

        # 递归+双指针法
        def recur(s, i ,j):
            if i > j:
                return []
            else:
                s[i], s[j] = s[j], s[i]
                recur(s, i + 1, j - 1)
        
        recur(s, 0, len(s) - 1)