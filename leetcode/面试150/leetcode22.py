from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []
        def dfs(l ,r):
            if l < r or l > n or r > n:
                return
            if l == n and r == n:
                res.append(''.join(path))
                return

            path.append('(')
            dfs(l + 1, r)
            path.pop()

            path.append(')')
            dfs(l, r + 1)
            path.pop()


        dfs(0, 0)
        return res