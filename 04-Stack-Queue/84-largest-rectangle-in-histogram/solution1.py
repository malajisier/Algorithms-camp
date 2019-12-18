# best solution:  https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
# 思路：
# 维护一个单调递增栈，有效地找出左边界。依次入栈，当前元素小于栈顶元素时，说明其右边界已找到，根据左右边界计算max面积

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # trick：在heights、stack分别添加0，-1，防止栈不为空时，还需要弹出栈中所有元素，分别计算最大面积
        heights.append(0)
        stack = [-1]
        maxarea = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                # h = heights[stack.pop()]
                # w = i - stack[-1] - 1 
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        # 防止栈不为空
        # heights.pop()
        return maxarea 

