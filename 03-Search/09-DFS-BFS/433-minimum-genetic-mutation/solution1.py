# BFS，迭代法

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # set查找效率高，O(1)
        bank = set(bank)
        if end not in bank:
            return -1

        q = [(start, 0)]
        # 每个基因对应的可变化的基因
        change = {
            'A': 'TCG', 
            'T': 'ACG', 
            'C': 'ATG', 
            'G': 'ATC'
            }

        while q:
            node, step = q.pop(0)
            if node == end:
                return step
            
            # 当前序列的每一个基因
            for i, v in enumerate(node):
                # 该基因相应的可以改变的基因
                for j in change[v]:
                    new = node[:i] + j + node[i + 1:]
                    if new in bank:
                        # 该序列若存在于bank，入队继续BFS
                        q.append((new, step + 1))
                        bank.remove(new)

        return -1