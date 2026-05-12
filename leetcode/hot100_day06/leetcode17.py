from typing import List, Optional

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res, path = [], []
        n = len(digits)
        def dfs(cur):
            if cur == n:
                res.append(''.join(path))
                return

            for c in dic[digits[cur]]:
                path.append(c)
                dfs(cur + 1)
                path.pop()

        dfs(0)
        return res

