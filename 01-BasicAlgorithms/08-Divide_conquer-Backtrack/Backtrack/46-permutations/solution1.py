# 回溯问题的建议：先画出递归树，理清执行过程 
# https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, n, depth, path, used, res):
            if depth == n:
                res.append(path[:])
                return 

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, n, depth + 1, path, used, res)

                    # 回溯，撤销上一次的选择并重置状态
                    used[i] = False
                    path.pop()
            
        n = len(nums)
        if n == 0: return []

        # 标记数组，O(1)时间里判断当前数是否被选择过，空间换时间
        # 使用基于交换的实现方法，也可省略used标记数组
        used = [False for _ in range(n)]
        res = []

        dfs(nums, n, 0, [], used, res)
        return res

# 优化：使用set来代替布尔标记数组
