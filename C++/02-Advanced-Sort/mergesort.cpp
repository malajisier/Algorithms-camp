// 自顶向下的递归实现

#include <iostream>
#include <algorithm>
#include "insertion_sort.h"
#include "utils.h"

using namespace std;

// 归并 arr[l...mid] 和 arr[mid+1...r] 两部分
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


template<typename T>
void __mergeSort(T arr[], int l, int r) {
    if (l >= r)
        return;
    
    int mid = (l + r) / 2;
    __mergeSort(arr, l, mid);
    __mergeSort(arr, mid + 1, r);
    __merge(arr, l, mid, r);

    // // 在近乎有序的数组中，通过判断mid来优化
    // if (arr[mid] <= arr[mid + 1])
    //     __mergeSort(arr, l, mid, r);
}


template<typename T>
void mergeSort(T arr[], int n) {
    __mergeSort(arr, 0, n - 1);
}


int main() {
    // test1：无序数组的排序
    int n = 50000;
    int* arr1 = utils::generateRandomArray(n, 0, n);
    int* arr2 = utils::copyIntArray(arr1, n);

    utils::testSort("Insertion sort:", insertionSort, arr1, n);
    utils::testSort("Merge sort", mergeSort, arr2, n);

    delete[] arr1;
    delete[] arr2;

    cout << endl;

    // test2：近乎有序的数组排序
    int swapTimes = 10;
    int* arr3 = utils::generateNearlrOrderedArray(n, swapTimes);
    int* arr4 = utils::copyIntArray(arr3, n);

    utils::testSort("Insertion sort:", insertionSort, arr3, n);
    utils::testSort("Merge sort", mergeSort, arr4, n);

    delete[] arr3;
    delete[] arr4;

    cout << endl;


    return 0;
}