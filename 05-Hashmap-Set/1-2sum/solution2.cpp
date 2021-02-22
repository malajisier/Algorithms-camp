#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;

        while (l < r) {
            if (nums[l] + nums[r] == target) {
                int res = {l + 1, r + 1};
                return vector<int>(res, res + 2);
            }
            else if (nums[l] + nums[r] < target) 
                l++;
            else
                r--;
        }
    }
};