# 多种方法详细解释：https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/

# 思路：
# 当前左右括号都有大于 00 个可以使用的时候，才产生分支；
# 产生左分支的时候，只看当前是否还有左括号可以使用；
# 产生右分支的时候，还受到左分支的限制，右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以产生分支；
# 在左边和右边剩余的括号数都等于 00 的时候结算

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            # 左右括号都为0，再结算
            if left == 0 and right == 0:
                res.append(cur_str)
                return 
            
            if right < left:
                return
            
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res