# https://leetcode-cn.com/problems/permutations/solution/quan-pai-lie-by-leetcode-solution-2/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first == n:
                res.append(nums[:])
            
            # 将nums划成左右两部分，左侧[0, first-1]表示已经填过的数，右侧[first,n-1]表示未填的数
            # 在递归搜索时动态维护这个数组

            # 在[first, n-1]里搜索未填过的数
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        if n == 0: return []

        res = []
        backtrack(0)
        return res

