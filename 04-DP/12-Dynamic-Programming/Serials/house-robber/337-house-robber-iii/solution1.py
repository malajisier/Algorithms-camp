# 递归 + 树形DP

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dp(root):
            res = [0, 0]
            if not root: return res

            left = dp(root.left)
            right = dp(root.right)

            res[0] += max(left[0], left[1]) + max(right[0], right[1])
            res[1] += left[0] + right[0] + root.val

            return res
        
        ans = dp(root)
        return max(ans[0], ans[1])


# 简洁版
class Solution:
    def dp(self, cur: TreeNode) -> List[int]:
        if not cur: return [0, 0]

        l = self.dp(cur.left)
        r = self.dp(cur.right)

        return [max(l) + max(r), l[0] + r[0] + cur.val]

    def rob(self, root: TreeNode) -> int:
        return max(self.dp(root))