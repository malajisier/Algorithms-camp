# 题目中有坑，比如 -E-16 测试时不是数值，与65题相同


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        dot = e = digit = False

        for i, char in enumerate(s):
            if char in ('+', '-'):
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False

            elif char == '.':
                if dot or e: 
                    return False
                dot = True

            elif char == 'e' or char == 'E':
                if e or not digit:
                    return False
                # 重置digit为False，以免e为最后一个char
                e, digit = True, False

            elif char.isdigit():
                digit = True

            else:
                return False

        return digit
