#include <iostream>
#include <vector>
#include <unordered_map>
#include <cassert>

using namespace std;

// 使用字典方法的C++写法
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> record;
        for (int i = 0 ; i < nums.size() ; i++)
            record[nums[i]] = i;

        for (int j = 0 ; j < nums.size() ; j ++) {
            unordered_map<int, int>::iterator iter = record.find(target - nums[j]);
            if(iter != record.end() && iter->second != j)
                return {j, iter->second};
        }
        throw invalid_argument("the input has no solution");
    }
};

void print_vec(const vector<int>& vec) {
    for(int e : vec)
        cout << e << " ";
    cout << endl;
}

int main() {
    vector<int> nums = {1, 2, 3, 4};
    int target = 6;
    print_vec(Solution().twoSum(nums, target));

    return 0;
}