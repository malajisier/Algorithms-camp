归并排序（分治） 
过程：
- 把长度为n的输入序列分成两个长度为n/2的子序列
- 对这两个子序列分别采用归并排序
- 将两个排序好的子序列合并一个最终的排序序列   

复杂度：
- 时间复杂度均为O(nlogn)
- 自顶向下，使用数组时，空间复杂度是 O(n+logn), logn: 调用系统栈的深度

```java
public class MergeSort {
    public int mergeSort(int[] nums) {
            aux = new int[nums.length];
            sort(nums, 0, nums.length - 1);        
        }
    public void sort(int[] nums, int left, int right) {
        if (left >= right) return;
        int mid = (left + right) / 2;
        sort(nums, left, mid);
        sort(nums, mid + 1, right);
        merge(nums, left, mid, right);
    }

    private void merge(int[] nums, int left, int mid, int right) {
        int i = left, j = mid + 1;
        for (int k = left; k <= right; k++) {
            aux[k] = nums[k];
        }

        int p = left;
        while (i <= mid || j <= right) {
            if (i > mid) nums[p++] = aux[j++]; // 左边已有序，只看右边
            else if (j > right) nums[p++] = aux[i++]; // 右边已有序
            else if (aux[i] <= aux[j]) nums[p++] = aux[i++]; // 选两边中较小的
            else nums[p++] = aux[j++];  
        }
    }
}
```