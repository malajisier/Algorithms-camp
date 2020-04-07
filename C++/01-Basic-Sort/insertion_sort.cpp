// 插入排序：
// 将每一个元素插入到前面合适的位置

#include <iostream>
#include "utils.h"
#include "selection_sort.h"

using namespace std;

template<typename T>
void insertionSort(T arr[], int n) {
    for (int i = 1; i < n; i++) {
        // 判断条件 可简化为：
        // for (int j = i; j > 0 && arr[j] < arr[j - 1]; j--)
        for (int j = i; j > 0; j--)
            if (arr[j] < arr[j - 1])
                swap(arr[j], arr[j - 1]);
            else
                break;
            
    }
}


template<typename T>
void insertionSortPro(T arr[], int n) {
    for (int i = 1; i < n; i++) {
        // 寻找当前元素合适的插入位置，减少交换次数
        T e = arr[i];
        // j 保存元素e，应该插入的位置
        int j;

        // 如果当前位置的前一个元素，比e 还大
        for (j = i; j > 0 && arr[j - 1] > e; j--)
            // e不能插入的位置，将其位置元素后移
            arr[j] = arr[j - 1];
        arr[j] = e;
    }
}



int main() {
    int n = 10000;
    int *arr1 = utils::generateRandomArray(n, 0, n);
    int *arr2 = utils::copyIntArray(arr1, n);
    int *arr3 = utils::copyIntArray(arr1, n);

    utils::testSort("Insertion Sort", insertionSort, arr1, n);
    utils::testSort("Insertion Sort Pro", insertionSortPro, arr2, n);
    utils::testSort("Selection Sort", selectionSort, arr3, n);

    delete[] arr1;
    delete[] arr2;
    delete[] arr3;

    return 0;
}