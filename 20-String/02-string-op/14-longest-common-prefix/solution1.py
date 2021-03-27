# 利用python特性，不推荐   
# 取每一个单词的，同一个位置比较    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        
        return res
