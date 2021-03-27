// 二维状态数组，定义房子编号和偷或不偷的情况      


class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        int n = nums.length;
        int[][] a = new int [n][2];

        // 0 表示不偷， 1 表示偷
        a[0][0] = 0;
        a[0][1] = nums[0];

        for (int i = 1; i < n; ++i) {
            // 第i个不偷，则最大值 就等于 第i-1个偷或不偷
            a[i][0] = Math.max(a[i - 1][0], a[i - 1][1]);
            // 第i个偷，则 最大值 就等于 第i - 1不偷 + 偷当前i
            a[i][1] = a[i - 1][0] + nums[i];
        }

        return Math.max(a[n - 1][0], a[n - 1][1]);
    }
}   