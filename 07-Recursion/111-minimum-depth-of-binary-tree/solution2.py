# DFS，使用辅助栈，TC: O(n), SC: O(n)

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            stack, mindep = [(root, 1)], float('inf')

        while stack:
            root, depth = stack.pop()
            children = [root.left, root.right]

            if not any(children):
                mindep = min(mindep, depth)
            
            # 不是叶子节点就压栈
            for c in children:
                if c:
                    stack.append((c, depth + 1))
        
        return mindep