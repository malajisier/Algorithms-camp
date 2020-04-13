class Solution:
    def printNumbers(self, n: int) -> List[int]:
        # max = 0
        # while n > 0:
        #     max = max * 10 + 9
        #     n -= 1
        
        return [i for i in range(1, 10 ** n)]