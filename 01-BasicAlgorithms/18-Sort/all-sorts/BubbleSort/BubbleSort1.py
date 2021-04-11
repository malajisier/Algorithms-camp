# 优化1：设置条件提前结束不必要的循环
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 标记这一趟遍历是否发生了数据交换，没有发生则说明已经排好序了
        # 因此不用再迭代了
        flag = False
        for j in range(1, n - i):
            if arr[j] < arr[j - 1]:
                arr[j], a[j - 1] = arr[j - 1], a[j]
                flag = True

        if flag: break
    
    return arr


# 优化2：标记最后一次发生 数据交换的位置
def bubble_sort_pro(arr):
    n = len(arr)
    k = n

    for i in range(n):
        flag = True
        for j in range(1, k):   #只遍历到最后交换的位置即可
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j - 1], arr[j]
                # 记录最后交换的位置
                k = j
                flag = False
        
        if flag: break

    return arr


