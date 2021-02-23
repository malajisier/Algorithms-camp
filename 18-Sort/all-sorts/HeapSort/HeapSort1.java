public class HeapSort1 {
    public static void main(String[] args) {
        int[] n = {6,5,2,7,3,9,8};
        System.out.println("Before Sort: " + Arrays.toString(n));
        
        heapSort(n);
        System.out.println("After Sort: " + Arrays.toString(n));
    }
    
    public static void heapSort(int[] n) {
        for (int i = n.length - 1; i >= 1; i--) {
            buildHeap(n, i);
            swap(n, 0, i);
        }
    }
    
    public static void buildHeap(int[] n, int end) {
        int len = end + 1;
        // 从最后一个 非叶节点开始比较
        for (int i = len / 2 -1; i >= 0; i--) {
            // i节点的 左右子节点
            int left = 2 * i + 1, right = 2 * i + 2;
            int maxone = left;
            if (right <= len - 1 && n[left] < n[right]) {
                maxone = right;
            }
            if (n[i] < n[maxone]) {
                swap(n, i, maxone);
            }
        }
    }
    
    // 待排序数组、下标
    private static void swap(int[] n, int i, int j) {
        int temp = n[i];
        n[i] = n[j];
        n[j] = temp;
    }
}