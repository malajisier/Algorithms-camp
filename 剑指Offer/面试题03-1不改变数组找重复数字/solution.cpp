// 题目描述：
// 给定长度n+1的数组nums，数组中的数均在1～n范围内，n>= 1，找出数组中任意一个不重复的数，且不能修改数组
// 思路：二分搜索法+抽屉原理，TC:O(logn)

class Solution {
public:
    int duplicateArray(vector<int>& nums) {
        int l = 1, r = nums.size() - 1;
        while (l < r) {
            int mid = l + r >> 1;
            int s = 0;
            // 计算左半部分长度
            for (auto x : nums) s += x >= l && x <= mid;
            if (s > mid - l + 1) 
                r = mid;
            else    
                l = mid + 1;
        }

        return r;
    }
}


