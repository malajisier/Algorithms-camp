class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int k = 0; k < nums.length - 2; k++) {
            if (nums[k] > 0) break;
            if (k > 0 && nums[k] == nums[k - 1]) continue;

            int l = k + 1, r = nums.length - 1;
            while (l < r) {
                int sum = nums[k] + nums[l] + nums[r];
                if (sum > 0) {
                    r--;
                } else if (sum < 0) {
                    l++;
                } else {
                    res.add(new ArrayList<Integer>(Arrays.asList(nums[k], nums[l], nums[r])));
                    
                    // 这种写法会超时
                    // while (l < r && nums[l] == nums[l + 1]) l++;
                    // while (l < r && nums[r] == nums[r - 1]) r--;
                    
                    while (l < r && nums[l] == nums[++l]);
                    while (l < r && nums[r] == nums[--r]);
                }
            }
        }

        return res;
    }
}