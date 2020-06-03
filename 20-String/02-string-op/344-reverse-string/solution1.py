# 解法一：双指针法  
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s: return 
        i, j = 0, len(s) -1 

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


# 解法二：抽象成函数，递归法
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def recur(s, left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                recur(s, left + 1, right - 1)
        
        recur(s, 0, len(s) - 1)

