class Solution:
    def reverseWords(self, s: str) -> str:
        # 首先去除头尾空格
        s = s.strip()

        res = ""
        # j 取到总长度，因为列表遍历区间是前闭后开的
        # i 负责探到空格， j 负责指向每个单词的最后一个字符
        i, j = len(s) - 1, len(s)

        # 从后往前遍历
        while i > 0:
            if s[i] == ' ':
                # 每遇到一个空格，添加其后的单词
                res += s[i + 1 : j] + ' '
                
                # while 负责去除中间单个或多个的空格
                while s[i] == ' ':
                    i -= 1

                # 单词的最后一个位置，因为list左闭右开，需取到i+1    
                j = i + 1

            # 每轮完成后，更新i，j的位置    
            i -= 1
        
        return res + s[: j]