# 从第一个元素开始，该元素可以认为已经被排序
# 取出下一个元素，在已经排序的元素序列中从后向前扫描
# 如果被扫描的元素（已排序）大于新元素，将该元素后移一位
# 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 将新元素插入到该位置后
# 重复步骤2~5


def insert_sort(arr):
    n = len(arr)

    for i in range(1, n):
        k = i - 1
        # 记录当前位置元素的值，不能省略
        mark = arr[i]
        # 新元素小于已排序元素时，依次往后挪一位
        while k >= 0 and arr[k] > mark:
            arr[k + 1] = arr[k]
            k -= 1
        arr[k + 1] = mark

    return arr

if __name__ == '__main__':
    arr = [9,1,2,6,3,7,0]
    print(insert_sort(arr))