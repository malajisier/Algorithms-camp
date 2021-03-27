#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        // set<int> record;
        // for (int i = 0; i < nums1.size(); i++) 
        //     record.insert(nums1[i]);

        // set<int> res;
        // for (int i = 0; i < nums2.size(); i++)
        //     // 如果不指向尾指针
        //     if (record.find(nums2[i]) != record.end())
        //         res.insert(nums2[i]);
        
        // // C++常用其迭代器，来遍历容器类
        // vector<int> res_vec;
        // for (set<int>::iterator iter = res.begin(); iter != res.end(); iter++)
        //     res_vec.push_back(*iter);

        // return res_vec;


        // 代码精简后
        set<int> record(nums1.begin(), nums1.end());
        set<int> res;
        for (int i = 0; i < nums2.size(); i++)
            if (record.find(nums2[i]) != record.end())
                res.insert(nums2[i]);

        return vector<int>(res.begin(), res.end());
    }
};