# 总体思路和方法一一样

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    
                # ,的作用没搞懂
                parens += p,
            return parens
        return generate('', n, n)