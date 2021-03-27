// 题目：请合并所有重叠的区间
// 输入: intervals = [[1,4],[4,5]]
// 输出: [[1,5]]

class solution1 {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals,(v1, v2) -> v1[0] - v2[0]);
        int[][] res = new int[intervals.length][2];
        int idx = -1;

        for (int[] interval: intervals) {
            // 如果
            if (idx == -1 || interval[0] > res[idx][1]) {
                res[++idx] = interval;
            } else {
                res[idx][1] = Math.max(res[idx][1], interval[1]);
            }
        }
        return Arrays.copyOf(res, idx + 1);
    }
}