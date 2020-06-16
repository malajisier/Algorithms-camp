# 使用栈，单独存所有字母
# TC:O(N), SC:O(N)

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # isalpha() 方法检测字符串是否只有字母组成，返回值为真假
        letters = [c for c in S if c.isalpha()]
        res = []

        for c in S:
            if c.isalpha():
                res.append(letters.pop())
            else:
                res.append(c)
        
        return ''.join(res)