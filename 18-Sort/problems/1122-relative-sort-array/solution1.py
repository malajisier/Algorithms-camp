# 计数排序
# TC：O(n+m),arr1,arr2的长度， SC:O(n)

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = [0 for _ in range(1001)]
        res = []

        # 统计arr1元素出现次数，下标为元素，值为出现次数
        for i in range(len(arr1)):
            arr[arr1[i]] += 1

        for i in range(len(arr2)):
            # arr2的元素在arr1的出现次数>0时
            while arr[arr2[i]] > 0:
                res.append(arr2[i])
                arr[arr2[i]] -= 1
        
        for i in range(len(arr)):
            # 把剩余arr1的元素添加到队尾
            while arr[i] > 0:
                # 注意这里，元素是下标
                res.append(i)
                arr[i] -= 1
        
        return res