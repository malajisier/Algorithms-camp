class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        # flag 标记空格
        count, flag = 0, 0

        for i in s[::-1]:
            # 去除尾部的空格
            if i == ' ' and flag == 0:
                continue

            # 遇到字符，开始计数
            if i != ' ':
                count += 1
                flag = 1
            
            # 再遇到空格，因为flag=1，直接跳出循环
            else:
                break
        
        return count