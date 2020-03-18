# 思路：一层一层的遍历添加，BFS
class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        res = []
        cur_level = [root]
        while cur_level:
            tmp = []
            next_level = []

            for node in cur_level:
                tmp.append(i.val)
                # 把当前结点的左右结点加到下一层
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            res.append(tmp)
            cur_level = next_level
        
        return res
            