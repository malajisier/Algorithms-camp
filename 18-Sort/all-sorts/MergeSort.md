归并排序（分治）       
过程：
- 把长度为n的输入序列分成两个长度为n/2的子序列
- 对这两个子序列分别采用归并排序
- 将两个排序好的子序列合并一个最终的排序序列   




（1）实现一：自顶向下    
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

（2）自底向上  
复杂度：
- 时间复杂度均为O(nlogn)
- 空间复杂度是 O(n), 使用了数组，但使用链表可以降到 O(1)，参考lc148    

```java
package com.wes.sort;
import java.util.Arrays;

// 自底向上的归并排序
public class MergeSortBU {
    public static void mergeSortBU(int[] arr, int n) {
        // 从最下面一层到顶，每一轮 归并区间里的个数：1，2，4...
        for (int sz = 1; sz <= n; sz += sz) {
            // 每一次归并的区间：每隔两个size归并一次，i的范围:i < n，但左侧边界限制：i+size < n
            for (int i = 0; i + sz < n; i += 2*sz) {
                // 归并的前提是两个区间都存在，右侧边界限制: min(区间右边界，arr右边界)
                 merge(arr, i, i + sz - 1, Math.min(i + 2*sz - 1, n - 1));
            }
        }
    }

    public static void merge(int[] arr, int left, int mid, int right) {
        int i = left, j = mid + 1;
        int[] aux = new int[right - left + 1];

        int p = 0;
        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) aux[p++] = arr[i++];
            else aux[p++] = arr[j++];
        }
        while (i <= mid) aux[p++] = arr[i++];
        while (j <= right) aux[p++] = arr[j++];

        for (int p1 = left, p2 = 0; p2 < aux.length; p1++, p2++) {
            arr[p1] = aux[p2];
        }
    }

    public static void main(String[] args) {
        int[] nums = {7,5, 6, 4,6,2,0,1,1,7};
        mergeSortBU(nums, nums.length);
        System.out.println(Arrays.toString(nums));
    }
}
```

