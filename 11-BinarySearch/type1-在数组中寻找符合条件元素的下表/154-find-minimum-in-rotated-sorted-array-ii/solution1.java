/**
 * 关于 left、mid、right 大小情况的讨论
 * https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/er-fen-fa-fen-zhi-fa-python-dai-ma-by-liweiwei1419/
 */

class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int l = 0, r = n - 1;

        while (l <= r) {
            int mid = l + (r - l) / 2;
            
            // mid>r，mid 是左边的最大元素，最小元素在 区间[mid+1, r] 
            if (nums[mid] > nums[r]) {
                l = mid + 1;
            // 同理
            } else if (nums[mid] < nums[r]) {
                r = mid;
            // 相等就排除一个边界
            } else {
                r--;
            }
        }
        return nums[l];
    }
}