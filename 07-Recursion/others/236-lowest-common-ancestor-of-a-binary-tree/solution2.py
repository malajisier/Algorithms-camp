# 使用父指针迭代，通过回溯p、q的父节点，找到的第一个公共节点即是最近公共祖先

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parents = {root: None}

        # p、q都找到时，才能结束循环
        while p not in parents or q not in parents:
            node = stack.pop()

            # 把每个节点的父节点都加入字典
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = parents[p]
        
        while q not in ancestors:
            q = ancestors[q]
        
        return q


            
