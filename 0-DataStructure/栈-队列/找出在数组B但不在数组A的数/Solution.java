public class Solution {
    // 二分法，也就是将 B 的每个数都利用二分法在 A 中进行查找
    private static List<Integer> getAllNotIncluded(int[] A, int[] B) {
        List<Integer> res = new ArrayList<>();
        // for 循环用于访问 B 中的每个数
        for (int i = 0; i < B.length; i++) {
            int left = 0;
            int right = A.length - 1;
            boolean contains = false;

            while (left <= right) {
                int middle = left + ((right - left) >> 1);
                // 由于是二分法，则需要一个 middle
                // 如果当前 B 中的元素一开始就等于 A 中的 A[middle] 的话，就说明包含，则直接跳出
                if (A[middle] == B[i]) {
                    contains = true;
                    // 跳出 while
                    break;
                }
                // 从 A 中的左半部分开始查找
                if (A[middle] > B[i]) {
                    right = middle - 1;
                    // 从 A 中的右半部分开始查找
                } else {
                    left = middle + 1;
                }
            }
            // B 中的数在 A 中找不到的话，说明 B 中的某个数不在 A 中，则将 B 中当前的数添加到结果集中
            if (!contains) {
                res.add(B[i]);
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[] a = {1, 2, 4, 6, 7};
        int[] b = {9, 6, 3};
        List<Integer> list = getAllNotIncluded(a, b);
        System.out.println(list);
    }
}