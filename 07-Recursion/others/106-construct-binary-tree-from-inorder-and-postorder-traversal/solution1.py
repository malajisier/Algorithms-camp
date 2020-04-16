# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 官方题解有详细解释
# 后序遍历的最后一个节点是根节点，中序遍历则将左右子树划分了出来
# TC:O(N), SC:O(N)

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):   
            if in_left > in_right: return None
            
            val = postorder.pop()
            root = TreeNode(val)
            idx = idxmap[val]
 
            root.right = helper(idx + 1, in_right)
            root.left = helper(in_left, idx - 1)
            return root
        
        idxmap = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)


# # 递归的另一种写法： TC:O(nlogn), SC:O(n)
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#         assert len(inorder) == len(postorder)

#         if len(inorder) == 0: return None
#         if len(inorder) == 1: return TreeNode(inorder[0])

#         root = TreeNode(postorder[-1])
#         pos = inorder.index(postorder[-1])

#         root.left = self.buildTree(inorder[:pos], postorder[:pos])
#         root.right = self.buildTree(inorder[pos + 1:], postorder[pos: -1])

#         return root