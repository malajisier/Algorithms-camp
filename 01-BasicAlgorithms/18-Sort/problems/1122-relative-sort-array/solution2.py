# 使用集合模块，利用字典来做
# TC & SC: O(1001)
import collections

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    
        count = collections.Counter(arr1)
        res = []

        for i in arr2:
            if count[i]:
                # count.pop(i)弹出元素i出现的次数，相应元素也随之删除
                res.extend([i] * count.pop(i))

        for i in range(1001):
            if count[i]:
                res.extend([i] * count.pop(i))

        return res