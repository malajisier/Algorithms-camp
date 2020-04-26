// 回溯的C++实现，可使用unordered_map代替map
// unordered_map：底层hash表实现，查找插入O(1)，map：红黑树实现，查找log(n),插入是log(n)+balance time

class Solution {
public:
    void backtrack(unordered_map<int, int>& m, int i, int n, vector<int>& visited, vector<vector<int>>& res) {
        if (i == n) {
            res.push_back(visited);
            return;
        }

        for (auto& p : m) {
            if (p.second == 0) continue;

            --p.second;
            visited.push_back(p.first);
            backtrack(m, i + 1, n, visited, res);

            ++p.second;
            visited.pop_back();
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        unordered_map<int, int> m;
        // map统计每个数的出现次数，避免dfs递归时重复取相同的数，相当于剪枝
        for (auto x : nums) ++m[x];

        vector<vector<int>> res;
        vector<int> visited;

        backtrack(m, 0, nums.size(), visited, res);
        return res;
    }
};