class Solution {
    public int[] twoSum(int[] nums, int target) {

        // 法一：使用set
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (!set.contains(target - num)) set.add(num);
            else return new int[]{num, target - num};
        }

        return new int[]{};



        // 双指针
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int s = nums[l] + nums[r];
            if (s == target) return new int[]{nums[l], nums[r]};
            else if (s > target) r--;
            else l++;
        }
        return new int[]{};
    }
}