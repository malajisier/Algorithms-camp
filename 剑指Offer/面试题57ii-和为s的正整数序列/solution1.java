// 滑动窗口实现
// TC:O(target), 两个指针均单调不减，所以最多移动target/2次，  SC:O(1)

class Solution {
    public int[][] findContinuousSequence(int target) {
        List<int[]> res = new LinkedList<int[]>();
        
        for (int l = 1, r = 2; l < r;) {
            // 等差数列求和
            int sum = (l + r) * (r - l + 1) / 2;
            if (sum == target) {
                int[] tmp = new int[r - l + 1];
                for (int i = l; i <= r; i++) {
                    tmp[i - l] = i;
                }
                res.add(tmp);
                l++;
            } else if (sum < target) {
                r++;
            } else {
                l++;
            }
        }
        return res.toArray(new int[res.size()][]);
    }
}


// 精简版 滑动窗口
class Solution {
    public int[][] findContinuousSequence(int target) {
        int l = 1, r = 1, sum = 0;
        List<int[]> res = new ArrayList<>();
        while (l <= target/2) {
            if (sum < target) {
                sum += r;
                r++;
            } else if (sum > target) {
                sum -= l;
                l++;
            } else {
                int[] tmp = new int[r - l];
                for (int i = l; i < r; i++) tmp[i - l] = i;
                res.add(tmp);
                sum -= l;
                l++;               
            }
        }
        return res.toArray(new int[res.size()][]);
    }
}