class BinarySearchImpl {
    public static void main(String[] args) {
        int[] arr = {1,8,2,5,34,65,7,12,237,6};

        int idx1 = recBinarySearch(arr, 1, 0, arr.length - 1);
        System.out.println(idx1);

        int idx2 = loopBinarySearch(arr, 2);
        System.out.println(idx2);
    }

    public static int recBinarySearch(int[] arr, int key, int low, int high) {
        int middle = (low + high) / 2;
        if (arr[middle] > key) {
            return recBinarySearch(arr, key, low, middle - 1);
        } else if (arr[middle] < key) {
            return recBinarySearch(arr, key, middle + 1, high);
        } else { 
            return middle;
        }
    }

    public static int loopBinarySearch(int[] arr, int key) {
        int low = 0;
        int high = arr.length - 1;

        while (low < high) {
            int middle = (low + high) / 2;
            if (arr[middle] > key) {
                high = middle - 1;
            } else if (arr[middle] < key) {
                low = middle + 1;
            } else {
                return middle;
            }
        }

        return -1;
    }
}