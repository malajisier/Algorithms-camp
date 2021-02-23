# n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数

# 示例：
#  [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#  ]

# 给定 target = 5，返回 true。



# 思路：从右上角或左下角查找   
def find(target, array):
    # 这里从右上角开始查找，
    # 右上角：每一行的最大数，每一列的最小数
    # TC：O(m+n)
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

