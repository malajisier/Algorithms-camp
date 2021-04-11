public class QuickSort1 {
    public static void QuickSort(int arr[], int left, int right) {
        int pivot;
        if (left < right) {
            pivot = partition(arr, left, right);
            QuickSort(arr, left, pivot - 1);
            QuickSort(arr, pivot + 1, right);
        }

    public static int partition(int arr[], int left, int right) {
        int pivot = arr[left];
        while (left < right) {
            while (left < right && arr[right] >= pivot) right--;
            if (left < right) arr[left++] = arr[right];

            while (left < right && arr[left] <= pivot) left++;
            if(left < right) arr[right--] = arr[left];
        }
        arr[left] = pivot;
        return left;
    }
    }
} 