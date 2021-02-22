// 非常好的示例代码，简洁高效，并且是严格意义上的归并排序，没有调用系统的排序方法，TC：O(nlogn)

public class Solution {
    public int reversePairs(int[] nums) {
        if (nums == null || nums.length == 0)
            return 0;
        return mergeSort(nums, 0, nums.length - 1);
    }

    private int mergeSort(int[] nums, int l, int r) {
        if (l >= r)
            return 0;
        int mid = l + (r - l ) / 2;
        int count = mergeSort(nums, l, mid) + mergeSort(nums, mid + 1, r);

        int[] temp = new int[r - l + 1];
        int i = l, k = l, t = 0;

        // merge之前统计逆序对，并且代替系统的sort
        for (int j = mid + 1; j <= r; j++, t++) {
            // 统计逆序对
            while (i < mid && nums[i] <= 2 * (long)nums[j]) i++;

            // sort，
            while (k <= mid && nums[k] < nums[j]) temp[t++] = nums[k++];
            temp[t] = nums[j];
            // 累加每一轮循环的逆序对
            count += mid - i + 1;
        }
        // 加入左半部分剩余的元素
        while (k <= mid)
            temp[t++] = nums[k++];
        // 把temp排好序的元素依次，复制到nums
        System.arraycopy(temp, 0, nums, l, r - l + 1);
        return count;
    }
}