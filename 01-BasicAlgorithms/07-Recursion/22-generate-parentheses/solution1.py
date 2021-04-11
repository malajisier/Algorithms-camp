class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self._generate('', 0, 0, n, res)
        return res

    def _generate(self, s, left, right, n, res):
        # lr=n，左右括号都已经用完
        if left == n and right == n:
            res.append(s)
            return res

        # 左括号还没有用完
        if left < n:
            self._generate(s + '(', left + 1, right, n, res)

        # 隐含条件：left > right and right < n
        # 但根据left<n，可直接得出l>r
        if left > right:
            self._generate(s + ')', left, right + 1, n, res)