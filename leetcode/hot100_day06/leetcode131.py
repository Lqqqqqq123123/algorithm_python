from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        n = len(s)

        def is_huiwen(s : str):
            return s == s[::-1]

        def dfs(start):
            if start == n:
                res.append(path[:])
                return
            for i in range(start, n):
                sub = s[start: i + 1]
                if is_huiwen(sub):
                    path.append(sub)
                    dfs(i + 1)
                    path.pop()

        dfs(0)
        
        return res