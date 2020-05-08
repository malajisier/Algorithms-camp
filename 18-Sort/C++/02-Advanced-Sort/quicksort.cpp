#include <iostream>
#include "insertion_sort.h"
#include "mergesort.h"
#include "utils.h"

using namespace std;


template<typename T>
int __partition(T arr[], int l, int r) {
    T e = arr[l];
    int j = l;

    for (int i = l + 1; i <= r; i++) {
        if (arr[i] < e) {
            swap(arr[j + 1], arr[i]);
            j ++;
        } 
    }

    swap(arr[l], arr[j]);
    return j;
}


template<typename T>
void __quickSort(T arr[], int l, int r) {
    if (l >= r)
        return;

    int p = __partition(arr, l, r);
    __quickSort(arr, l, p - 1);
    __quickSort(arr, p + 1, r);
}


template<typename T>
void quickSort(T arr[], int n) {
    __quickSort(arr, 0, n - 1);
}


int main() {
    // test1：无序数组的排序
    int n = 50000;
    int* arr1 = utils::generateRandomArray(n, 0, n);
    int* arr2 = utils::copyIntArray(arr1, n);
    int* arr3 = utils::copyIntArray(arr1, n);

    utils::testSort("Insertion sort:", insertionSort, arr1, n);
    utils::testSort("quickSort", quickSort, arr2, n);
    utils::testSort("Merge sort", mergeSort, arr3, n);


    delete[] arr1;
    delete[] arr2;
    delete[] arr3;

    cout << endl;

    // test2：近乎有序的数组排序
    int swapTimes = 10;
    int* arr4 = utils::generateNearlrOrderedArray(n, swapTimes);
    int* arr5 = utils::copyIntArray(arr4, n);
    int* arr6 = utils::copyIntArray(arr4, n);

    utils::testSort("Insertion sort:", insertionSort, arr4, n);
    utils::testSort("quickSort", quickSort, arr5, n);
    utils::testSort("Merge sort", mergeSort, arr6, n);

    delete[] arr4;
    delete[] arr5;
    delete[] arr6;
    cout << endl;

    return 0;
}