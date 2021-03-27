# 整数是2的幂次方，它的二进制只含有一个1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n != 0 and (n & (n - 1)) == 0



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return n & (n - 1) == 0