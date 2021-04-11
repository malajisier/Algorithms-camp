# 法二：使用辅助栈,一层一层的把雨水计算出来 TC:O(N), SC:O(N)
# https://leetcode-cn.com/problems/trapping-rain-water/solution/bao-li-jie-fa-yi-kong-jian-huan-shi-jian-zhi-zhen-/

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0
        stack = []

        for i in range(n):
            # 当前元素大于栈顶元素时，说明其就是右边界
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack:
                    break
                h = min(height[i], height[stack[-1]]) - height[tmp]
                w = i - stack[-1] - 1
                res += h * w
            stack.append(i)

        return res
