class Solution:
    def hammingWeight(self, n: int) -> int:
        # 调用系统函数，转为二进制
        return bin(n).count('1')


class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        count = 0
        for c in n:
            if c == '1':
                count += 1
        
        return count