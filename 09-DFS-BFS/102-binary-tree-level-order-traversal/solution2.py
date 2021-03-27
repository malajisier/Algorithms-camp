# 思路：与方法1相似，使用辅助的队列deque来提升性能，（python中的queue，为了多线程间的交换安全使用了锁，所以性能不佳）


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        res = []
        level = 0
        dq = collections.deque([root,])

        while dq:
            res.append([])
            curlev_len = len(dq)

            for i in range(curlev_len):
                node = dq.popleft()
                res[level].append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            level += 1

        return res





