import java.util.*;
// 小根堆构建
/**
 * 堆排序 求前m小元素，构建 m次小根堆，每次排序后的头部元素就是最小的
 * 注意：
 * （1）索引从 1开始到 n，方便左右孩子计算: 2*i, 2*i+1
 * （2）
 */
public class HeapSort2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        
        int[] arr = new int[n + 1];
        for (int i = 1; i <= n; i++) arr[i] = sc.nextInt();
        
        int size = n;
        for (int i = size / 2; i > 0; i--) down(arr, size, i);
        
        while (m-- > 0) {
            // // 可封装成函数: 弹出头部元素，剩余的再构建成小根堆
            // System.out.print(arr[1] + " ");
            // arr[1] = arr[size];
            // size--;
            // down(arr, size, 1);
            
            System.out.print(pop(arr, size) + " ");
        }
    }
    
    public static void down(int[] arr, int size, int u) {
        int p = u;
        int left = 2 * u, right = 2 * u + 1;
        if (left <= size && arr[left] < arr[p]) p = left;
        if (right <= size && arr[right] < arr[p]) p = right;
        if (p != u) {
            swap(arr, p, u);
            down(arr, size, p);
        }
    }
    
    public static void swap(int[] arr, int i, int j) {
        int tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
    }

    public static int pop(int[] arr, int size) {
        int top = h[1];
        h[1] = h[size--];
        down(arr, size, 1);
        return top;
    }
}