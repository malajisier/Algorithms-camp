// 回溯的C++版本

class Solution {
public:
    vector<vector<int>> res;
    
    vector<vector<int>> combine(int n, int k) {
        if (k <= 0 || n <= 0 || k > n) return res;
        vector<int> track;
        backtrack(1, n, k, track);
        return res;
    }

    void backtrack(int start, int n, int k, vector<int>& track) {
        if (k == track.size()) {
            res.push_back(track);
            return;
        }

        for (int i = start; i <= n; i ++) {
            track.push_back(i);
            backtrack(i + 1, n, k, track);
            track.pop_back();
        }
    }
};