 # 迭代法，逐一列举
  
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # pynic最简版
        res = [[]]
        for num in nums:
            res = [[num] + subset for subset in res]
        return res

        # # 详细版
        # res = [[]]
        # for num in nums:
        #     newsets = []
        #     for subset in res:
        #         newsub = subset + [num]
        #         newsets.append(newsub)
        #     res.extend(newsets)                          
        # return res
                                                                                                                            


