# 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        cur_len = 0
        max_len = 0
        
        # 利用set的性质，是用哈希表实现的，查找效率高，O(1)
        lookup = set()

        for i in range(n):
            cur_len += 1

            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            
            max_len = max(max_len, cur_len)

        return max_len