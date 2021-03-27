# 从后往前贪心, TC:O(N)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False

        # 设置最后能达到的位置
        reach = len(nums) - 1
        # 从后往前贪心
        for i in range(reach, -1, -1):
            # 如果当前点能够跳到最后点
            if (nums[i] + i) >= reach:
                # 更新到最前面的点，即能跳到最后的点
                reach = i
        
        # 如果最后能到达起点，说明跳跃成功
        return reach == 0

