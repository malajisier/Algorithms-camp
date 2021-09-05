 // 玄学解法：不保证结果对错


class Solution {
    public boolean search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            // 二分时，把中点、两个端点一块检查
            if (nums[mid] == target || nums[left] == target || nums[right] == target) {
                return true;
            } else if (nums[left] < target && target < nums[mid]) {
                right = mid;
            } else if (nums[mid] < target && target < nums[right]) {
                left = mid;
            }
            left++;
            right--;
        } 
        return false;
    }
}