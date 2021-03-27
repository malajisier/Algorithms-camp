# BFS，最大深度=层次遍历后的深度
class Solution:
    def maxDepth(self, root: TreeNone) -> int:
        if not root:
            return 0

        queue = [(1, root)]
        while queue:
            depth, node = queue.pop(0)
            if node.left:
                queue.append((depth + 1, node.left))
            if node.right:
                queue.append((depth + 1, node.right))
            
        return depth

# DFS
class Solution:
    def maxDepth(self, root: TreeNone) -> int:
        if not root:
            return 0

        stack = [(1, root)]
        depth = 0
        while stack:
            cur_dep, node = queue.pop(0)
            depth = max(depth, cur_dep)

            # 使用辅助栈(先入后出)，需要先将右孩子入栈
            if node.right:
                stack.append((depth + 1, node.right))
            if node.left:
                stack.append((depth + 1, node.left))
            
            
        return depth


