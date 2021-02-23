class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def gen(start, end):
            if start > end:
                return [None,]
            
            allTrees = []
            for i in range(start, end + 1):
                leftTrees = gen(start, i - 1)
                rightTrees = gen(i + 1, end)

                for l in leftTrees:
                    for r in rightTrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        allTrees.append(root)
            
            return allTrees
        
        return gen(1, n) if n else []
            