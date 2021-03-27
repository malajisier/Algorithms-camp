# 使用集合set，TC:O(n+m), SC:O(n)

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jset = set(J)
        return sum(s in jset for s in S)