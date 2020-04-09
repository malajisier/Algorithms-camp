#include <iostream>
#include <cassert>
using namespace std;

namespace utils{
    // 返回指向数组第一个元素的指针
    int *generateRandomArray(int n, int rangeL, int rangeR){
        assert(rangeL <= rangeR);

        int *arr = new int[n];
        /* key:
     *  srand(): 随机数发生器的初始化函数
     *  rand(): %是限定随机生成的整数的取值范围， 例: 生成[m,n]范围内的数， rand() % (n-m+1)+m
     *  每次调用前都会查询是否调用过srand(seed)
     */
        srand(time(NULL));
        for (int i = 0; i < n; i++)
            arr[i] = rand() % (rangeR - rangeL + 1) + rangeL;
        return arr;
    }

    
    // 生成近乎有序的数组，swapTimes来随机交换数据
    int *generateNearlrOrderedArray(int n, int swapTimes) {
        int *arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = i;

        srand(time(NULL));
        for (int i = 0; i < swapTimes; i++) {
            int posx = rand()%n;
            int posy = rand()%n;
            swap(arr[posx], arr[posy]);
        }

        return arr;
    }


    template<typename T>
    void printArray(T arr[], int n) {
        for (int i = 0; i < n; i++)
            cout << arr[i] << " ";
        cout << endl;

        return;
    }


    template<typename T>
    bool isSorted(T arr[], int n) {
        for (int i = 0; i < n - 1; i++)
            if (arr[i] > arr[i + 1])
                return false;
        return true;
    }


    template<typename T>
    // 传入值：函数名，排序函数指针，测试数组及长度
    void testSort(string sortName, void(*sort)(T[], int), T arr[], int n){
        clock_t startTime = clock();
        sort(arr, n);
        clock_t endTime = clock();

        // assert(isSorted(arr, n));
        cout << sortName << ": " << double(endTime - startTime) / CLOCKS_PER_SEC << "s" << endl;

        return;
    }


    int* copyIntArray(int a[], int n) {
        int* arr = new int[n];
        // 拷贝：原数组的头指针，尾指针，目标地址的头指针
        copy(a, a + n, arr);
        return arr;
    }

}