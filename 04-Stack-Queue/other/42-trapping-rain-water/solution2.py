# 法二：使用辅助栈,TC:O(N)

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0
        stack = []

        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack:
                    break
                h = min(height[i], height[stack[-1]]) - height[tmp]
                w = i - stack[-1] - 1
                res += h * w
            stack.append(i)

        return res
