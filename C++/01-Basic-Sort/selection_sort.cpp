// 选择排序：
// 始终将最小元素放在首位，依次与最小元素比较

#include <iostream>
#include "utils.h"
using namespace std;

// 模板函数，可以比较不同类型的数组
template<typename T>
void selectionSort(T arr[], int n) {
    for(int i = 0; i < n; i++) {
        int minIndex = i;
        for(int j = i + 1; j < n; j++)
            if(arr[j] < arr[minIndex])
                minIndex = j;
        swap(arr[i], arr[minIndex]);
    }
}

int main() {
    int n = 10000;
    int *arr = utils::generateRandomArray(n, 0, 10000);
    // selectionSort(arr, 10000);
    // utils::printArray(arr, 10);

    utils::testSort("Selection Sort", selectionSort, arr, n);

    // 释放数组arr
    delete[] arr;

    return 0;
}