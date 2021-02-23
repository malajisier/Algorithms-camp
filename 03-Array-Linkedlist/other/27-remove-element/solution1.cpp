class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int idx = 0;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[i - 1])
                nums[idx++] = nums[i]; 
        }

        return idx;
    }
};