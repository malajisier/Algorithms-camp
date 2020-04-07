# 利用二叉搜索树的特性，中序遍历是有序的，44ms

class Solution:

    def isValidBST(self, root):
        stack = []
        inorder = float('inf')

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val <= inorder:
                return False
            
            inorder = root.val
            root = root.right

        
        return True