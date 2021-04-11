# 法一：双指针法，TC:O(N)
# 难点：在每一个位置能容下的雨水量等于它左右两边柱子最大高度的最小值减去它的高度
# 一个位置存雨水只和左右两边的柱子有关，

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right, res = 0, len(height) - 1, 0
        # 记录左右边最大值
        left_max = height[left]
        right_max = height[right]

        while left < right:
            if height[left] < height[right]:
                # 说明存在凹槽
                if left_max > height[left]: 
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if right_max > height[right]:
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return res 