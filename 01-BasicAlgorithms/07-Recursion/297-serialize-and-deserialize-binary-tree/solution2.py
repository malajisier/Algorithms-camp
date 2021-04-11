# BFS实现，时间复杂度优于DFS

from collections import deque

class Codec:
    def serialize(self, root):
        res = []
        dq = deque()

        if root: dq.appendleft(root)
        while dq:
            root = dq.pop()
            if root:
                res.append(str(root.val))
                dq.appendleft(root.left)
                dq.appendleft(root.right)
            else:
                res.append("#")
        
        return ",".join(res)

    def reserialize(self, data):
        if not data: return 

        data = iter(data.split(","))
        root = TreeNode(next(data))
        dq = deque([root])

        while dq:
            node = dq.pop()
            left_val = next(data)

            if left_val != "#":
                node.left = TreeNode(int(left_val))
                dq.appendleft(node.left)
            
            right_val = next(data)
            if right_val != "#":
                node.right = TreeNode(int(right_val))
                dq.appendleft(node.right)
        
        return root 
        