from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []

        def dfs(u, l, r):
            if r > l:
                return
            if u == 2 * n and l == r:
                res.append(''.join(path))
                return
            if l > n or r > n:
                return

                # 左括号
            path.append('(')
            dfs(u + 1, l + 1, r)
            path.pop()
            path.append(')')
            dfs(u + 1, l, r + 1)
            path.pop()

        dfs(0, 0, 0)

        return res
