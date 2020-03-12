# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 法二：迭代法，使用辅助栈
        res = []
        stack = []
        # p作为指针
        p = root

        while p or stack:
            # 先将左儿子全部压入栈中，最后p指向null，循环停止
            while p:
                stack.append(p)
                p = p.left
            
            p = stack.pop()
            res.append(p.val)

            # 指向右子树
            p = p.right
        
        return res

            