# 位运算技巧 x&(x-1)：清零最低位的1    
# TC:O(1), SC:O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1 
            n = n & (n - 1)
        return count 