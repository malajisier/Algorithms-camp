class Solution {
public:
    bool searchArray(vector<vector<int>> array, int target) {
        if (array.empty() || array[0].empty()) return False;

        int i = 0, j = array[0].size();
        while (i <= array.size() and j >= 0) {
            if (array[i][j]) return true;
            if (array[i][j] < target) i ++;
            else j --;
        }

        return false;
    }
}