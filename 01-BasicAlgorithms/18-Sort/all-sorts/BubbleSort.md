冒泡排序    
- 嵌套循环，每次比较相邻元素，若是逆序则交换
- 最坏、平均都是O(n^2)，最好O(n)：待排序列是升序序列，每次比较都不用交换
- 空间：O(1)  


```java
class BubbleSort {
    public static void bubbleSort(int[] nums) {
        for (int i = nums.length - 1; i > 0; i-- ) {
            for (int j = 0; j + 1 <= i; j++) {
                if (nums[j] > nums[j + 1]) {
                    int tmp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = tmp;
                }
            }
        }
    }
    
    // 冒泡排序 改进
    public static void bubbleSortPro(int[] nums) {
        for (int i = nums.length - 1; i > 0; i--) {
            // 设置标志位，看是否发生过交换
            boolean flag = false;
            for (int j = 0; j + 1 < i; j++) {
                if (nums[j] > nums[j + 1]) {
                    int tmp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = tmp;
                    flag = true;
                }
                // 没有交换操作，说明有序，提前结束
                if (!flag) break;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {4,1,1,2,9,4,3};
        bubbleSort(arr);
        System.out.println("bubble sort: " + Arrays.toString(arr));
        
        bubbleSortPro(arr);
        System.out.println("bubble sort: " + Arrays.toString(arr));
    }
}
```