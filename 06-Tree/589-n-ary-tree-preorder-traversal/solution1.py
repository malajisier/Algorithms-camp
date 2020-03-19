"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 迭代法
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack, res = [root,], []

        while stack:
            node = stack.pop()
            res.append(node.val)
            # 子节点，倒序推入栈中
            # extend()在列表末尾一次性追加，另一个序列的多个值
            stack.extend(root.children[::-1])

        return res
