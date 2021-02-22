/**
* 顺子的情况：
* （1）没有大小王，严格升序，例：12345
* （2）有一个大小王，例：01345, zeroCnt=diff=1
*  (3) 两个大小王，例：00245，->1 2 3 45,zero=diff=2
* （4）三个，例：00015,->10005, 
* （5）四个、五个，
* 
* 规律：zeroCnt >= diff
* TC:O(N)，虽然数组排序复杂度O(logn)，但for循环最差需要遍历整个数组，  
* SC:O(1)
*/

class Solution {
    public boolean isStraight(int[] nums) {
        Arrays.sort(nums);
        int zeroCnt = 0, diff = 0;

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == 0) {
                zeroCnt++;
            } else {
                if (nums[i] == nums[i + 1]) return false;

                // 排序后的相邻元素，差为2 的地方最多只能有两个
                if (nums[i] + 1 != nums[i + 1]) {
                    diff += nums[i + 1] - nums[i] - 1;
                }
            }
        }
        return zeroCnt >= diff;
    }
}