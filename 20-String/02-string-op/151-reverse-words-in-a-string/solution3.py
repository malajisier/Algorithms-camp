# https://leetcode-cn.com/problems/reverse-words-in-a-string/submissions/
# 使用双端队列，基本没使用语言内置的函数， TC:O(N),  SC:O(N)

class Solution:
    def reverseWords(self, s: str) -> str:
        l, r = 0, len(s) - 1

        # 去除头尾空格
        while l <= r and s[l] == ' ':
            l += 1
        
        while l <= r and s[r] == ' ':
            r -= 1
        
        dq = collections.deque()
        word = []

        # 从头部开始遍历
        while l <= r:
            # 不是空格时，把单个字符依次添加到word
            if s[l] != ' ':
                word.append(s[l])
            
            # 遇到空格，说明一个单词已经遍历完毕
            elif s[l] == ' ' and word:
                dq.appendleft(''.join(word))
                # 一个单词加到deque后，word置为空，方便后续循环添加，下一个单词的字符
                word = []

            l += 1
        
        dq.appendleft(''.join(word))
        return ' '.join(dq)
