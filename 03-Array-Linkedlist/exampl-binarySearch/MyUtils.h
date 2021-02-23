#include <iostream>
#include <cassert>

using namespace std;


namespace MyUtils {

    int *generateOrderedArray(int n) {
        assert( n > 0);
        int *arr = new int[n];

        for (int i = 0 ; i < n ; i++)
            arr[i] = i;
        
        return arr;
    }
};