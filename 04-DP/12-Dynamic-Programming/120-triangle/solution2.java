// https://leetcode-cn.com/problems/triangle/solution/di-gui-ji-yi-hua-sou-suo-zai-dao-dp-by-crsm/
// 递归法，普通递归会超时


// 记忆化搜索: 附加缓存的递归
class Solution {
    int row;
    Integer[][] memory;


    public int minimumTotal(List<List<Integer>> triangle) {
        row = triangle.size();
        memory = new Integer[row][row];
        return helper(0, 0, triangle);
    }

    private int helper(int level, int i, List<List<Integer>> triangle) {
        if (memory[level][i] != null) return memory[level][i];

        if (level == row - 1) {
            return memory[level][i] = triangle.get(level).get(i);
        }

        int left = helper(level + 1, i, triangle);
        int right = helper(level + 1, i + 1, triangle);

        return memory[level][i] = Math.min(left, right) + triangle.get(level).get(i);
    }
}