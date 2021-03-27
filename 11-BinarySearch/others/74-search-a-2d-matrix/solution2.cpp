// class Solution {
// public:
//     bool searchMatrix(vector<vector<int>>& matrix, int target) {
//         if (matrix.empty()) return false;

//         int n =  matrix.size(), m = matrix[0].size();
//         int row = 0, col = m;

//         while (row < n && col >= 0) {
//             if (matrix[row][col] < target) row ++;
//             else if (matrix[row][col] < target) col --;
//             else return true;
//         }

//         return false;
//     }
// };