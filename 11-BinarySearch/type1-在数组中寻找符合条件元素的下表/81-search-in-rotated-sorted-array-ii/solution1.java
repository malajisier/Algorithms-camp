/**
 * 对比 lc—33，nums中含有重复元素，时间复杂度可能退化到O(N)
 * https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/zai-javazhong-ji-bai-liao-100de-yong-hu-by-reedfan/
 */

class Solution {
    public boolean search(int[] nums, int target) {
        if (nums == null || nums.length == 0) return false;
        int left = 0, right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return true;
            }
            // 重复元素直接去掉，但重复元素过多时，几乎需要全部遍历，退化到O(N)
            if (nums[left] == nums[mid]) {
                left++;
                continue;
            }

            // 前半序列有序
            if (nums[left] < nums[mid]) {
                // mid元素 严格小于target，否则开始的判断 会直接返回true
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // mid元素 严格大于target，否则开始的判断 会直接返回true
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return false;
    }
}