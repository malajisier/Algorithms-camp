#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1;
        vector<int> res;

        for (int i : nums1)
            set1.insert(i);

        for (int i : nums2) {
            auto target = set1.find(i);
            if (target != set1.end()) {
                res.push_back(i);
                set1.erase(target);
            }
        }

        return res;

    }
};