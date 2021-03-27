# 回溯算法，
# https://leetcode-cn.com/problems/combinations/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-ma-/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k > n or k <= 0:
            return []
        
        res = []
        self.backtrack(1, n, k, [], res)
        return res 


    def backtrack(self, start, n, k, pre, res):
        # 终结当前层递归的条件
        if len(pre) == k:
            res.append(pre[:])
            return
        
        for i in range(start, n + 1):
            pre.append(i)
            # 下探下一层
            self.backtrack(i + 1, n, k, pre, res)

            # 当前层不满足条件时，回溯并重置状态
            pre.pop()


# 剪枝优化：递归时去掉一些，没必要走的步数
# 通过归纳法，可一进一步缩小i的范围，i < n  -->   i < n - (k - pre.size()) + 1  
    # for i in range(start, n - (k - pre.size()) + 2):
    #         pre.append(i)
    #         # 下探下一层
    #         self.backtrack(i + 1, n, k, pre, res)

    #         # 当前层不满足条件时，回溯并重置到上一层状态
    #         pre.pop()
