# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS，遍历每层记录下来，取每层最大值
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        dq = collections.deque()
        dq.append(root)

        # 如果使用普通列表当做队列，会慢20ms
        # dq = [root]
        res = []

        while dq:
            # 记录当前层的所有数字
            cur_nums = []

            # 只循环当前层大小的次数
            for _ in range(len(dq)):
                node = dq.popleft()
                # node = dq.pop(0)
                cur_nums.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(max(cur_nums))
        return res
