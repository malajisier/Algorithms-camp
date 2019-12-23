# 从右上角或左下角查找   

def find(target, array):
    # 这里从右上角开始查找
    rows = len(array) - 1
    cols = len(array) - 1
    i = 0
    j = cols

    while i <= rows and j >= 0:
        if target > array[i][j]:
            i += 1
        elif target < array[i][j]:
            j -= 1
        else:
            return True
    return False

print(find(41,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))

