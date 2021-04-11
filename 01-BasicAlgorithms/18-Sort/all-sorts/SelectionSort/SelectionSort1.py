# 步骤：
# （1）在未排序的序列中找到最小（大）元素，存放到排序序列起始的位置
# （2）在剩余序列中寻找最小（大）元素，放到已排序的 序列的末尾
# （3）重复1，2

def selection_sort(arr):
    n = len(arr)

    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]

    return arr
