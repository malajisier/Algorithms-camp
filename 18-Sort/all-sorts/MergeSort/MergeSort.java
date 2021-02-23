public class MergeSort {
    public static void main(String[] args) {
        int[] a = {2,4,1,34,6,0};
        System.out.println("Before Sort: " + Arrays.toString(a));
        
        quickSort(a, 0, 5);
        System.out.println("After Sort: " + Arrays.toString(a));
    }
    
    public static void quickSort(int[] array, int begin, int end) {
        if (end <= begin) return;
        int pivot = partition(array, begin, end);
        quickSort(array, begin, pivot - 1);
        quickSort(array, pivot + 1, end);
    }
    
    static int partition(int[] a, int begin, int end) {
        int pivot = end, counter = begin;
        for (int i = begin; i < end; i++) {
            if (a[i] < a[pivot]) {
                int tmp = a[counter];
                a[counter] = a[i];
                a[i] = tmp;
                counter++;
            }
        }
        int temp = a[pivot];
        a[pivot] = a[counter];
        a[counter] = temp;
        return counter;
    }
}    
}
