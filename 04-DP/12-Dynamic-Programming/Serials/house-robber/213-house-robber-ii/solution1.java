class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        return Math.max(helper(nums, 0, n - 2), helper(nums, 1, n - 1));
    }

    int helper(int[] nums, int start, int end) {
        int n = nums.length;
        int cur = 0, pre = 0, dp = 0;
        for (int i = end; i >= start; i--) {
            dp = Math.max(cur, pre + nums[i]);
            pre = cur;
            cur = dp;
        }

        return dp;
    }   
}