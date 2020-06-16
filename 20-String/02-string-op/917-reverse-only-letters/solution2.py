class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        res = []
        j = len(S) - 1

        for i, c in enumerate(S):
            if c.isalpha():
                while not S[j].isalpha():
                    j -= 1
                res.append(S[j])
                j -= 1
            else:
                res.append(c)
        
        return "".join(res)
        