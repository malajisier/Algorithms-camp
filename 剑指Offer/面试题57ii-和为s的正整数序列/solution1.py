class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l, r = 1, 2
        res = []

        while l <= target//2:
            cur_sum = sum(list(range(l, r + 1)))
            if cur_sum < target: r += 1
            elif cur_sum > target: l += 1
            else:
                res.append(list(range(l, r + 1)))
                l += 1
        
        return res