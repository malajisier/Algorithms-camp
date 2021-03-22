选择排序       
- 过程：每次找最小值，然后放到 待排序数组的起始位置
- 时间复杂度：因为每次都需要在后面找最小值，来插入到平均、最好最坏都是O(n^2)
- 空间复杂度：O(1)  


```java
public class SelectionSort {
    public static void selectionSort(int[] arr) {
        int len = arr.length;
        for (int i = 0; i < len - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < len; j++) {
                if (arr[j] < arr[minIndex]) minIndex = j;
            }
            swap(arr, i, minIndex);
        }
    }

    private static void swap(int[] nums, int index1, int index2) {
        int tmp = nums[index1];
        nums[index1] = nums[index2];
        nums[index2] = tmp;
    }

    public static void main(String[] args) {
        int[] a = {4,3,2,1};
        System.out.println(Arrays.toString(a));

        selectionSort(a);
        System.out.println(Arrays.toString(a));
    }
}
```

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]

    return arr
```

