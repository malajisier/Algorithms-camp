class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        //　双指针法,标注最后一个不为零元素的位置
        int lastNonZero = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                nums[lastNonZero++] = nums[i];
            }
        }

        for(int j = lastNonZero; j < nums.size(); j++) {
            nums[j] = 0;
        }
    }
};