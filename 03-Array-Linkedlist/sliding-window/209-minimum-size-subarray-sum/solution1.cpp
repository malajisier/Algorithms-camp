// 滑动窗口法，若sum<s，右边界+1，否则左边界+1

#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        // [l, r], 初始化窗口
        int l = 0, r = -1;
        int sum = 0, res = nums.size() + 1;

        while (l < nums.size()) {
            // 保证右边界不越界
            if(r + 1 < nums.size() && sum < s)
                sum += nums[++r];
            else
                // sum过大时，左边界缩小
                sum -= nums[l++];

            if (sum >= s)
                res = min(res, r - l + 1);
        }
        
        if (res == nums.size() + 1)
            return 0;
        return res;
    }
};


int main() {

    vector<int> nums1 = {2, 3, 1, 2, 4, 3};
    int s1 = 7;
    cout << Solution().minSubArrayLen(s1, nums1) << endl;

    return 0;
}