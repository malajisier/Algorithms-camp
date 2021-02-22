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