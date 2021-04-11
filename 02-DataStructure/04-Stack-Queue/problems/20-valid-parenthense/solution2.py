# 思路大致相似，这里用到了一个小技巧：
# 解决边界问题：
# 首先在左右括号对应的map中添加对应的'?','?'
# 给stack赋初值'?'，这样stack pop时不会报错

class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['?']
        dic = {'[': ']', '(': ')', '{': '}', '?': '?'}
        for bkt in s:
            if bkt in dic:
                stack.append(bkt)
            elif dic[stack.pop()] != bkt:
                return False
        return len(stack) == 1