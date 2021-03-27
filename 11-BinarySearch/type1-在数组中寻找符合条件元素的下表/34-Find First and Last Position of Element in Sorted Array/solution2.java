/**
 * 复杂的版本，需要依次找出 开始位置和结束位置
 * https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/da-jia-bu-yao-kan-labuladong-de-jie-fa-fei-chang-2/
 */

class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums.length == 0) {
            return new int[]{-1, -1};
        }
        int begin = findBeginPosition(nums, target);
        if (begin == -1) return new int[]{-1, -1};
        int last = findLastPosition(nums, target);
        return new int[]{begin, last};
    }

    // 寻找开始位置，
    private int findBeginPosition(int[] nums, int target) {
            int l = 0, r = nums.length - 1;

            while (l <= r) {
                int mid = l + (r - l) / 2;
                // mid 可能不是第一个 出现target的位置
                if (nums[mid] == target) {
                    // 继续向左边找，即 [left, mid - 1] 区间里找
                    r = mid - 1;
                } else if (nums[mid] < target) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }

            if (l != nums.length && nums[l] == target) {
                return l;
            }
            return -1;
        } 
        
        private  int findLastPosition(int[] nums, int target) {
            int l = 0, r = nums.length - 1;

            while (l <= r) {
                int mid = l + (r - l) / 2;
                // mid 可能不是最后一个出现 target的位置，继续向右寻找
                if (nums[mid] == target) {
                    l = mid + 1;
                } else if (nums[mid] < target) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
            // findFirstPosition 方法可以返回是否找到，这里无需单独再做判断
            return r;
        }
}