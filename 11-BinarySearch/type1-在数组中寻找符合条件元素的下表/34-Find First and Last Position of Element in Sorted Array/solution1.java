/**
 * 改进版的二分查找
 * https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/javaer-fen-fa-gai-zao-3chong-fang-shi-du-ji-bai-li/
 */

class Solution {
    public int[] searchRange(int[] nums, int target) {
        // 查找第一个出现的target，作为 开始位置   
        int first = helper(nums, target);

        if (first < nums.length && nums[first] == target) {
            // 往后寻找 结束位置
            int last = helper(nums, target + 1) - 1;
            return new int[]{first, last};
        }
        return new int[]{-1, -1};
    }

    
    public static int helper(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            // 严格小于target的元素，一定不存在解，到[mid+1, r]中寻找
            if (nums[mid] < target) {
                l = mid + 1;

            // 判断条件是：nums[mid] >= target，需要注意：两者相等时，mid 可能不是第一个target的位置，需要往左找第一个出现的位置
            // 所以要去[l, mid-1]中寻找
            } else {
                r = mid - 1;
            }
        }
        return l;
    }
}