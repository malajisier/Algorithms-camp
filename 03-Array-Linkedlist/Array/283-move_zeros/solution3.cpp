#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    // 时间复杂度：O(n)
    // 空间复杂度：O(n)
    void moveZeroes(vector<int>& nums) {
        vector<int> nonZero;

        for (int i = 0; i < nums.size(); i++) 
            if (nums[i])
                nonZero.push_back(nums[i]);

        for (int i = 0; i < nonZero.size(); i++)
            nums[i] = nonZero[i];

        for (int i = nonZero.size(); i < nums.size(); i++)
            nums[i] = 0;  
    }


public:
    void moveZeroes1(vector<int>& nums) {
        // 不开辟新空间，SC：O(1)
        int lastNonZero = 0;  // 标注最后一个不为零元素的位置
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                nums[lastNonZero++] = nums[i];
            }
        }

        for(int j = lastNonZero; j < nums.size(); j++) {
            nums[j] = 0;
        }
    }


public:
    void moveZeroes2(vector<int>& nums) {
        int k = 0;
        for (int i = 0; i < nums.size(); i++)
            if (nums[i])
                if (i != k)
                    swap(nums[k++], nums[i]);
                else
                    k++;
    }
};

int main() {
    int arr[] = {0, 1, 0, 10, 15};
    vector<int> vec( arr, arr + sizeof(arr) / sizeof(int) );

    Solution().moveZeroes1( vec );

    for( int i = 0 ; i < vec.size() ; i ++ )
        cout << vec[i] << " ";
    cout << endl;

    return 0;
}