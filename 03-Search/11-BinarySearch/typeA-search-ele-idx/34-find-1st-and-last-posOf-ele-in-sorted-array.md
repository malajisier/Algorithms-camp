```java
// 不包含 target的左右边界

public int getRight(int[] nums, int target) {
    int l = 0;
    int r = nums.length - 1;
    int rightBorder = -2;

    while (l <= r) {
        int mid = l + (r - l) /2;
        // target 在[l, mid-1]
        if (nums[mid] > target) {
            r = mid - 1;
        } else { // nums[mid] <= target
            l = mid + 1;
            rightBorder = l;
        }
    }
    return rightBorder;
}


public int getLeft(int[] nums, int target) {
    int l = 0;
    int r = nums.length - 1;
    int leftBorder = -2;

    while (l <= r) {
        int mid = l + (r - l) / 2;
       
        // target 在[l, mid]区间里，mid-1 是第一个target左侧的数
        if (nums[mid] >= target) {
            r = mid - 1;
            leftBorder = r;
        // nums[mid] < target, 说明target 在[mid+1, r]区间
        } else { 
            l = mid + 1;
        }

        if (nums[mid] < target) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
}
```
