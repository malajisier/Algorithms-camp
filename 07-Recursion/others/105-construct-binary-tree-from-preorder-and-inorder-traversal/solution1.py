class Solution:
    def __init__(self):
        self.preorder = None
        self.pos = dict

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preSize = len(preorder)
        inSize = len(inorder)

        if preSize != inSize:
            return None
        self.preorder = preorder
        self.pos = dict()
        for i in range(inSize):
            self.pos[inorder[i]] = i;

        return self.recBuild(0, preSize - 1, 0, inSize - 1);

    def recBuild(self, pl, pr, il, ir):
        if pl > pr or il > ir:
            return None
        
        root_pos = self.preorder[pl];
        pivot = self.pos[root_pos];
        root = TreeNode(root_pos);

        root.left = self.recBuild(pl + 1, pl + pivot - il, il, pivot);
        root.right = self.recBuild(pl + pivot - il + 1, pr, pivot + 1, ir);
        return root


# # 简洁版的递归  
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if len(inorder) == 0:
#             return None
        
#         # 根节点
#         root = TreeNode(preorder[0])
#         # 获取根节点在 inorder 中的索引
#         idx = inorder.index(preorder[0])
#         # 左子树
#         root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
#         # 右子树
#         root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
#         return root
