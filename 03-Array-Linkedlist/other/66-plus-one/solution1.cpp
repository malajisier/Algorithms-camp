// 模拟竖式计算进位，然只需要加11即可。对此，我们将问题分成以下3类：

// 给定整数中最后一位不是数字99（如12341234）；
// 给定整数中最后一位是数字99，但不全是数字99（如10991099）；
// 给定整数所有位全是数字99（如99999999）。
// 算法思路：

// 对于上述情况1，直接在最后一位加11即可。
// 对于上述情况2，只需从后向前遍历数组，逢99进11，直至非99结束。
// 对于上述情况3，我们在最开始不需要与情况2区分，只需要在按照情况2遍历结束后判断首位，若首位为00，则代表情况3出现，此时直接在vector末尾添加1个00，再将首位由00变为11即可。

using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (digits[i] != 9) {
                digits[i]++;
                return digits;
            }
            else {
                digits[i] = 0;
            }
        }
        digits.push_back(0);
        digits[0] = 1;
        return digits;
    }
};