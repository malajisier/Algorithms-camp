# 迭代法，使用辅助栈将递归转化为迭代，深度优先搜索快一些，68ms
class Solution:
    def isValidBST(self, root):
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'),]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))

        return True

