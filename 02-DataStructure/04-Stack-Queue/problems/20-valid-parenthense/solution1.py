# 思路：
# 遇到左括号压栈；遇到右括号，和栈顶元素比较。若匹配，栈顶元素弹出，否则为False
# TC:O(n), SC: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'[': ']', '(': ')', '{': '}'}
        for bkt in s:
            if bkt in dic:
                stack.append(bkt)
                continue
            if dic[stack[-1]] == bkt:
                stack.pop()
            else:
                return False
        # 只有stack为空时才为True，否则说明stack有未匹配的左括号
        return True if not stack else False