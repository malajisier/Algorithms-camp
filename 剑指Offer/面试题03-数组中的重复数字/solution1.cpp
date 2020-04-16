// 按照原书，还有一个要求：数组中的数字可能不在0~n-1的范围内，或者数组不包含重复数字，返回-1
// 思路：数组内部元素交换，把数字交换到对应的位置，直到不能交换
// TC:O(N), SC:O(1)

class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        int n = nums.size();
        // 提前遍历确定数的范围
        for (auto x : nums)
            if (x < 0 || x >= n) 
                return -1
        
        // 从头开始遍历，把每个数交换到其对应的位置
        for (int i = 0; i < n; i ++) {
            // 当前的数和坑不匹配，当前坑和坑里的数不匹配时
            while (i != nums[i] && nums[nums[i]] != nums[i]) swap(nums[i], nums[nums[i]]);
            不能交换时，判断是否有重复数
            // nums[i]没在正确位置 或者 nums[i]要放的位置已经有数了
            if (nums[i] != i && nums[nums[i]] == nums[i]) return nums[i];
        }

        return -1;
    }
};