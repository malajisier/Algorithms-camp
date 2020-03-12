// 三路快排
// 把整体元素划分为三个子区间，指针zero、two分别指向元素0的最后一个、元素2的第一个
// [0, zero]     0
// [zero+1, two) 1
// [two, len-1]  2

#include <vector>
#include <cassert>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        
        // 初始化[0, zero]保证为空
        int zero = -1;
        // 初始化[two, len-1]保证为空
        int two = nums.size();

        // i == two 覆盖了三个子区间
        for (int i = 0; i < two; ) {
            if (nums[i] == 1)
                i ++;
            else if (nums[i] == 2) {
                // 元素为2时，与two指针的前一个元素相交换
                two --;
                swap(nums[i], nums[two]);
            }

            else {
                // 保证其他元素干扰
                assert(nums[i] == 0);
                // 元素为0时，与zero指针的后一个元素相交换
                zero ++;
                swap(nums[zero], nums[i]);

                i ++;
            } 
        }
    }
};