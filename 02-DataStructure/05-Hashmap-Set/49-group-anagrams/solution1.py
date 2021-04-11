class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in sorted(strs):
            key = tuple(sorted(s))
            dic[key] = dic.get(key, []) + [s]
        
        return dic.values()


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = []
#         dic = {}
#         for s in strs:
#             keys = "".join(sorted(s))
#             if keys not in dic:
#                 dic[keys] = [s]
#             else:
#                 dic[keys].append(s)
#         return list(dic.values())