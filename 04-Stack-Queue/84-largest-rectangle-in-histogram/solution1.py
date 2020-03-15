# best solution:  https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms

# 思路： 找到第i 位置的最大面积，即以第i根柱子为最矮柱子所能延伸的最大面积
# 以i为中心，向左找出第一个小于heights[i]的左边界，向右找出第一个小于heights[i]的右边界
# 维护一个单调递增栈，有效地找出左边界。依次入栈，当前元素小于栈顶元素时，说明其右边界已找到，根据左右边界计算max面积

# TC:O(N)
# SC:O(N)，使用辅助栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # trick：在heights、stack分别添加0，-1，防止栈不为空时，还需要弹出栈中所有元素，分别计算最大面积
        heights.append(0)
        stack = [-1]
        maxarea = 0

        for i in range(len(heights)):
            # 当前元素小于栈顶元素时，说明这是右边界
            while stack and heights[i] < heights[stack[-1]]:
                # h = heights[stack.pop()]
                # w = i - stack[-1] - 1 
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        return maxarea 


