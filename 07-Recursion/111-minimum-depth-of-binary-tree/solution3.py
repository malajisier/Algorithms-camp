# BFS，按照树的层去迭代，第一个访问到叶子节点的就是最小深度的节点
# 避免DFS遍历所有节点的缺点
# TC: O(n), SC: O(n)


from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            dq = deque([(root, 1)])

        while dq:
            root, depth = dq.popleft()
            children = [root.left, root.right]

            # 第一次下探到叶子节点时，就是最小深度
            if not any(children):
                return depth
            
            for c in children:
                if c:
                    dq.append((c, depth + 1))

