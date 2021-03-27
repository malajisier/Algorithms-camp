# 思路：递归法，DFS，左右结点 按照其所在的层对应添加

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        res = []

        def helper(node, level):
            # 递归到第几层，相对应的就增加这个层的[]
            if len(res) == level:
                res.append([])
            
            res[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return res
