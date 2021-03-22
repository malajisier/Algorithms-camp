插入排序      
- 过程：对于未排序的数据，在已排序序列中从后往前扫描，找到相应位置插入
- 时间复杂度：最坏、平均都是O(n^2)，最好O(n)：待排序列是降序序列，每次直接插到头部

```java
public class InsertionSort {
    public static  int[] insertionSort(int[] nums) {
        int len = nums.length;
        for (int i = 0; i < len; i++) {
            int tmp = nums[i];
            int j = i;
            // 寻找插入位置
            while (j > 0 && nums[j - 1] > tmp) {
                nums[j] = nums[j - 1];
                j--;
            }
            nums[j] = tmp;
        }
        return nums;
    }

    public static void main(String[] args) {
        int[] a = {4,3,2,1};
        System.out.println(Arrays.toString(a));

        insertionSort(a);
        System.out.println(Arrays.toString(a));
    }
}
```


```python
def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        k = i
        cur = nums[i]
        while k > 0 and nums[k - 1] > cur:
            nums[k] = nums[k - 1]
            k -= 1
        nums[k] = cur
    return nums

if __name__ == '__main__':
    nums = [5,1,0,2,4,3]
    insert_sort(nums)
```