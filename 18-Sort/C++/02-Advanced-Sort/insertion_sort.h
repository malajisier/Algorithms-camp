#include <iostream>
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
