#include <iostream>
#include <ctime>
#include <cassert>
#include "MyUtils.h"

using namespace std;

template<typename T>
int binarySearch( T arr[], int n, T target) {
    int l = 0, r = n - 1;
    while (l <= r) {
        int mid = (l + r) / 2;
        if( arr[mid] == target )
            return mid;
        if( arr[mid] < target )
            l = mid + 1;
        else
            r = mid - 1;
    }
    return -1;
} 



int main() {
    int n = 10000;
    int* data = MyUtils::generateOrderedArray(n);

    clock_t start = clock();
    for ( int i = 0 ; i < n ; i ++ )
        assert( i == binarySearch(data, n, i));
    clock_t end = clock();

    cout << "binarysearch test completed" << endl;
    cout << "Time Cost: " << double(end - start) / CLOCKS_PER_SEC << "s" << endl;

    return 0;
}