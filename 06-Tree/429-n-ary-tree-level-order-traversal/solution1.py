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
            next_lev = []
            tmp = []

            # 1.添加当前层结点的值  2.添加结点的儿子到下一层
            for node in cur:
                tmp.append(node.val)

                # 后者写法性能更好
                next_lev += node.children
                # for child in node.children:
                #     next_lev.append(child)
                    
            
            res.append(tmp)
            cur = next_lev
        
        return res