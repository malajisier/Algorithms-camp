"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 递归法，与二叉树的层次遍历类似
        def travel_node(node, level):
            if len(res) == level:
                res.append([])

            res[level].append(node.val)
            for child in node.children:
                travel_node(child, level + 1)
            

        res = []
        if root:
            travel_node(root, 0)
        
        return res 

        

                  