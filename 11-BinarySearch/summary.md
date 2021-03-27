二分查找的前提 
- 1.目标函数的单调性，递增或递减
- 2.存在上下界（bounded）
- 3.能够通过索引访问   

代码模板 
```Python
left, right = 0, len(array) - 1
while left < right:
    # 强类型语言里，r+l可能会越界
    # 可以用 left + (right - left) / 2 代替
    mid = (left + right) // 2
    if array[mid] == target:
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1 
```