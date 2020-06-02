# for循环列表生成式    
# 但时空复杂度不怎么好


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([s for s in S if s in J])