// 使用数组实现最大堆
// shiftUp：向上移动元素来调整堆
// shiftDown：移出堆顶元素时，对调队尾元素，向下移动元素来调整堆

#include <iostream>
#include <algorithm>
#include <string>
#include <ctime>
#include <cmath>
#include <cassert>

using namespace std;

template<typename Item>
class MaxHeap {

private:
    Item* data;
    int count;
    // 可优化的点：根据元素数量灵活调整数组大小
    int capacity;

    // 向上移动元素，保证堆的正确性
    void shiftUp(int k) {
        // 防止k 引起的数组越界
        while (k > 1 && data[k / 2] < data[k]) {
            swap(data[k / 2], data[k]);
            k /= 2;
        }
    }

    void shiftDown(int k) {
        // 保证有左孩子
        while (k * 2 <= count) {
            // 此轮循环，data[k] 和 data[j] 交换位置
            int j = 2 * k;
            // 是否有右孩子，右孩子是否大于左孩子
            if (j + 1 <= count && data[j + 1] > data[j])
                j += 1;
            
            if (data[k] >= data[j])
                break;
            
            swap(data[k], data[j]);
            k = j;
        }
    }

public:
    MaxHeap(int capacity) {
        data = new Item[capacity + 1];
        count = 0;
        this->capacity = capacity;
    }

    ~MaxHeap() {
        delete [] data;
    }

    int size() {
        return count;
    }

    bool isEmpty() {
        return count == 0;
    }

    void insert(Item item) {
        assert(count + 1 < capacity);

        data[count + 1] = item;
        count ++;
        shiftUp(count);
    }

    Item extractMax() {
        assert(count > 0);
        Item res = data[1];

        // 对调堆顶元素和队尾元素
        swap(data[1], data[count]);
        count --;
        shiftDown(1);

        return res;
    }

};


int main() {
    MaxHeap<int> maxheap = MaxHeap<int>(100);

    srand(time(NULL));
    for (int i = 0; i < 15; i++)
        maxheap.insert(rand()%100);

    // maxheap.testPrint();

    return 0;
}