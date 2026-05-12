from typing import List, Optional

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        path, st = [], [False for _ in range(25)]
        def dfs(u):
            if u == n:
                res.append(list(path))
                return
            for i in range(n):
                if not st[i + 10]:
                    st[i + 10] = True
                    path.append(nums[i])
                    dfs(u + 1)
                    st[i + 10] = False
                    path.pop()

        dfs(0)
        return res

