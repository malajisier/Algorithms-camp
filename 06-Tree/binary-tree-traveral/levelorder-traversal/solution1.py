class solution1:
    def levelOrder(self, root):
        if root == None:
            return
        
        res = []
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)

