```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        // int n = nums.length;

        // int l = 0, r = n;
        // while (l < r) {
        //     int mid = (r + l) / 2;
        //     if (nums[mid] < target) {
        //         l = mid + 1;
        //     } else {
        //         r = mid;
        //     }
        // }
        // return l;


        int n = nums.length - 1;
        int l = 0, r = n - 1;
        while (l <= r) {
            int mid = l + (r - l)/2;
            if (nums[mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return l;
    }
}
```