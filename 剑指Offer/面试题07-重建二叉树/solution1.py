# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 全局变量可以使递归方法少传一些参数
    def __init__(self):
        self.preorder = None
        self.reverses = None

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preSize = len(preorder)
        inSize = len(inorder)
        # 可以省略，题目中的数据都是有效的
        if preSize != inSize:
            return None
        
        self.preorder = preorder
        self.reverses = dict()
        # 用dict，使寻找根节点在中序遍历的位置的TC变为O(1)
        for i in range(inSize):
            self.reverses[inorder[i]] = i
        
        return self.__build(0, preSize - 1, 0, inSize - 1)
    
    def __build(self, prel, prer, inl, inr):
        if prel > prer and inl > inr:
            return None

        # 每个新二叉的根节点，一定是前序的第一个元素
        pos = self.preorder[prel]
        pos_idx = self.reverses[pos]
        root = TreeNode(pos)

        root.left = self.__build(prel + 1, pos_idx - inl + prel, inl, pos_idx - 1)
        root.right = self.__build(pos_idx - inl + prel + 1, prer, pos_idx + 1, inr)

        return root