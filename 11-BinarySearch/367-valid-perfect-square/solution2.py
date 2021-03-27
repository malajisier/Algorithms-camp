# 数学特性： 利用等差数列： 1+3+5+..+(2N-1) = N^2

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        
        return num == 0
        
