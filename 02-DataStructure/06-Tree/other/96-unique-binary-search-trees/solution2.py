# https://leetcode-cn.com/problems/unique-binary-search-trees/solution/er-cha-sou-suo-shu-fu-xi-li-zi-jie-shi-si-lu-by-xi/

# 思路： 
# 1,2...n这个数列是递增的，所以从任意一个位置“提起” 这棵树，都满足二叉搜索树的这个条件：左儿子小于爸爸，右儿子大于爸爸

class Solution:
    def numTrees(self, n: int) -> int:
        store = [1,1] #f(0),f(1)
        if n <= 1:
            return store[n]
        for m in range(2,n+1):
            s = m-1
            count = 0
            for i in range(m):
                count += store[i]*store[s-i]
            store.append(count)
        return store[n]
