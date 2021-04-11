# 两种方法都属于计数排序
# 法一：比较排序后的俩字符串是否相等

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t):
            return False

        # 将第一个字符串，写入字典
        for ele in s:
            dic[ele] = dic.get(ele, 0) + 1

        # 比较第二个字符串
        for ele in t:
            if dic.get(ele, 0) < 1:
                return False
            else:
                dic[ele] -= 1
        return True
