# 双指针法,从两边向中间逼近     
# 关联题目： 1-two-sum，使用哈希表

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 写法一：
        # 先对原数组排序
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):                                  
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1; r -= 1
        return res





        # 写法二：
        nums.sort()
        
        n = len(nums)
        res, k = [], 0

        for k in range(n - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i, j = k + 1, len(nums - 1)
            while i < j:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res




