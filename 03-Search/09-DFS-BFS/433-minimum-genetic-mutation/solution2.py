# 递归回溯
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank: 
            return -1
        if not start or not end: 
            return -1

        bank = set(bank)
        change = {
            'A':'GCT',
            'G':'ACT',
            'C':'AGT',
            'T':'AGC'
        }

        def helper(node, count, _bank):
            # terminator
            if node == end: 
                steps.append(count)
            if not _bank: 
                return
            # process 
            for i, s in enumerate(node):
                for c in change[s]:
                    new = node[:i] + c + node[i + 1:]
                    if new in _bank:
                        _bank.remove(new)
                        # drill down 进入下一层的探索
                        helper(new, count + 1, _bank)
                        # reverse state 恢复现场 探索这层的其他分支
                        _bank.add(new)

        steps = []
        helper(start, 0, bank) 
        if not steps: 
            return -1
        else: 
            return min(steps)