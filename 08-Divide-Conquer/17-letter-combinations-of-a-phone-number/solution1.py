# pythonic 解法

class Solution:
    def letterCombinations(self, digits: str):
        numbers = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
            }

        if not digits:
            return []
        
        combs = ['']
        for i in digits:
            # 第一轮循环的结果存到了combs
            combs = [x + y for x in combs for y in numbers[i]]

        return combs