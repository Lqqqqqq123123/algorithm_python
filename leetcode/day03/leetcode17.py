from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }

        path, res = [], []
        n = len(digits)
        def dfs(u):
            if u == n:
                res.append(''.join(path))
                return

            for c in dic[int(digits[u])]:
                path.append(c)
                dfs(u + 1)
                path.pop()

        dfs(0)
        return res