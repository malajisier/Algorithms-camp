# 双指针法: 移动较短线指针尽管造成了矩形宽度的减小，但却可能会有助于面积的增大
# 时间复杂度：O(n)， 空间复杂度：O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_area = 0, len(height) - 1, 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# # 暴力解法，不推荐
# class Solution {
# public:
#     int maxArea(vector<int>& height) {
#         int max = 0;
#         for (int i = 0; i < height.size(); i++) {
#             for (int j = i + 1; j < height.size(); j++) {
#                 int h = Math.min(height[i], height[j]);
#                 if (h * (j - i) > max) {
#                     max = h * (j - i);
#                 }
#             }
#         }
#         return max;
#         }
# };