# 解法一：使用内置的API
# TC:O(n)
# SC:O(n), c可以做到O(1)的额外空间复杂度，因为python、java的语言特性，string是不可变的

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))