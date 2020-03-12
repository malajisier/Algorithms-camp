"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # BFS
        if not root:
            return []
        
        res = []
        cur = [root]

        while cur:
            next = []
            tmp = []

            for node in cur:
                tmp.append(node.val)
                next += node.children
            
            res.append(tmp)
            cur = next
        
        return res