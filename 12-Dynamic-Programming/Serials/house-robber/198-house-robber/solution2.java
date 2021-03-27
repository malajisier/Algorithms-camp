// 状态数组优化至一维：假设第i 个房子必偷

class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        // 要保证i>= 2，才能进行比较
        if (nums.length == 1) return nums[0];

        int n = nums.length;
        int[] a = new int[n];

        a[0] = nums[0];
        a[1] = Math.max(nums[0], nums[1]);
        int res = Math.max(a[0], a[1]);

        for (int i = 2; i < n; ++i) {
            // 假设第i 个必偷，只关心i-1， i-2偷或不偷的情况
            a[i] = Math.max(a[i - 1], a[i - 2] + nums[i]);
            res = Math.max(res, a[i]);
        }

        return res;
    }
}