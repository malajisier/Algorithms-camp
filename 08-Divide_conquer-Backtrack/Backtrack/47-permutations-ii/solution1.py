# 题目对于重复性有要求，基于46.solution1 做的剪枝优化，排除回溯中可能重复使用的数
# https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return
            
            for i in range(size):
                if not used[i]:

                    # ***需要剪枝的情况：当前数和上一次的数相同，并且上一次的数也刚刚被撤销，这样的数不剪枝在下面搜索中会被重复使用***
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

        
        size = len(nums)
        if size == 0: return []

        # 先将数组排序，方便剪枝的时候去除重复数字
        nums.sort()
        used = [False] * size
        res = []
        dfs(nums, size, 0, [], used, res)
        return res