# 中序遍历 + 提前返回
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return

            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)
        
        self.k = k
        dfs(root)
        return self.res