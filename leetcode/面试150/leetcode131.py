from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        n = len(s)

        def dfs(start: int):
            if start == n:
                return

            # 枚举终点
            for i in range(start, n):
                # 判断
                sub = s[start:i + 1]
                if sub == sub[::-1]:
                    path.append(sub)

                    dfs(i + 1)
                    path.pop()

        dfs(0)
        return res
