# 方法一：使用栈

class Solution:
    def reverseWords(self, s: str) -> str:
        stack, res = [], ""
        s = s + " "

        for i in s:
            stack.append(i)
            if i == " ":
                while stack:
                    res += stack.pop()

        return res[1:] 


# 方法二：语言特性   
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split(' ')[::-1])[::-1]

