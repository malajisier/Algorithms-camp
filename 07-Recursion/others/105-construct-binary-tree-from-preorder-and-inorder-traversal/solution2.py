# 迭代法，比较难想到，TC:O(n), SC:O(n)
# 详细在官方题解：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/solution/mian-shi-ti-07-zhong-jian-er-cha-shu-by-leetcode-s/
# 栈保存遍历过的节点，初始中序遍历的指针指向第一个元素，如果前序遍历的元素不等于中序遍历的指针指向的元素，则前序遍历的元素为上一个节点的左子节点
# 若想等，正向遍历中序遍历的元素同时反向遍历前序遍历的元素，找到最后一次相等的元素，将前序遍历的下一个节点作为最后一次相等的元素的右子节点
# 反向遍历前序遍历的元素可通过栈的弹出元素实现

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        stack = []
        index = 0
        root = TreeNode(preorder[0])
        stack.append(root)
        n = len(preorder)

        for i in range(1, n):
            preval = preorder[i]
            if inorder[i] != stack[-1].val:
                node = stack[-1]
                node.left = TreeNode(preval)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[index]:
                    node = stack[-1]
                    stack.pop()
                    index += 1
                node.right = TreeNode(preval)
                stack.append(node.right)
        return root
 
        