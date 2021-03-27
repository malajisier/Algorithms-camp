class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<char, int> rows[9], cols[9], sub[9];
        for (int i  = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.' 
                && (rows[i][board[i][j]]++ || cols[j][board[i][j]]++ || sub[i / 3 * 3 + j / 3][board[i][j]]++))
                    return false;
            }
        }
        return true;
    }
};