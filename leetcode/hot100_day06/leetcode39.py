from typing import List, Optional

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        n = len(candidates)

        def dfs(cur, sum):
            if sum == target:
                res.append(path[:])
                return
            if sum > target or cur == n:
                return


            # 枚举所有选择：当前这个数能选k次
            k = 0
            while sum + candidates[cur] * k <= target:
                dfs(cur + 1, sum + candidates[cur] * k)
                k += 1
                path.append(candidates[cur])

            # 回溯
            for i in range(k):
                path.pop()


        dfs(0, 0)
        return res

