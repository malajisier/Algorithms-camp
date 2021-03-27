# 使用set过滤重复元素，记录最大、最小值
# 是顺子的条件：差必须<5

# TC:O(N),     SC:O(N)
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        # 初始化
        max_poker, min_poker = 0, 14

        for num in nums:
            if num == 0: continue
            max_poker = max(max_poker, num)
            min_poker = min(min_poker, num)
            if num in repeat:
                return False
            repeat.add(num)
        
        # 含0个数：12345，02345，00245，00015，00005
        return max_poker - min_poker < 5