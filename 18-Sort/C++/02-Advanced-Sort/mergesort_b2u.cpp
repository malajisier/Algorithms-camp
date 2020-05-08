// 自底向上的递归实现
#include <iostream>
#include <algorithm>
#include "insertion_sort.h"
#include "utils.h"


template<typename T>
void __merge(T arr[], int l, int mid, int r) {
    // 使用辅助空间复制所有arr元素
    T aux[r - l + 1];
    for (int i = l; i <= r; i++)
        // arr从 l位置 开始 
        aux[i - l] = arr[i];
    
    // 三个指针，ij指向辅助空间中两部分的起始位置，k指向arr的起始位置
    int i = l, j = mid + 1;
    for (int k = l; k <= r; k++) {
        // 左半部分已经遍历结束，i 已经超过中间位置mid
        if (i > mid) {
            arr[k] = aux[j - l];
            j ++;
        }
        else if (j > r) {
            arr[k] = arr[i - l];
            i ++;
        }

        // 对比两半部分，位置上元素的大小
        else if (aux[i - l] < aux[j - l]){
            arr[k] = aux[i - l];
            i ++;
        }
        else {
            arr[k] = aux[j - l];
            j ++;
        }
    }
}


// 注意：自底向上的实现，虽然是两层for循环，但时间复杂度却为 nlogn， 可以在1秒之内轻松处理100万数量级的数据
// 这是个陷阱，不要轻易根据循环层数判断复杂度
// 而且没有使用到数组索引的特性，所以在对链表等数据结构进行排序时，比自顶向下的更加合适
template<typename T>
void mergeSortB2U(T arr[], int n) {
    for (int sz = 1; sz <= n; sz += sz) 
        // i + sz保证了不会越界, min保证了最后一部分，不足size大小的情况
        for (int i = 0; i < n - sz; i += sz + sz)
            // 对 arr[i...i+sz-1]、arr[i+sz...i+2*sz-1]进行归并
            __merge(arr, i, i + sz - 1, min(i + sz + sz - 1, n - 1));
}




int main() {
    // test1：无序数组的排序
    int n = 50000;
    int* arr1 = utils::generateRandomArray(n, 0, n);
    int* arr2 = utils::copyIntArray(arr1, n);

    utils::testSort("Insertion sort:", insertionSort, arr1, n);
    utils::testSort("Merge sort", mergeSortB2U, arr2, n);

    delete[] arr1;
    delete[] arr2;

    cout << endl;

    // test2：近乎有序的数组排序
    int swapTimes = 10;
    int* arr3 = utils::generateNearlrOrderedArray(n, swapTimes);
    int* arr4 = utils::copyIntArray(arr3, n);

    utils::testSort("Insertion sort:", insertionSort, arr3, n);
    utils::testSort("Merge sort", mergeSortB2U, arr4, n);

    delete[] arr3;
    delete[] arr4;

    cout << endl;
    return 0;
}