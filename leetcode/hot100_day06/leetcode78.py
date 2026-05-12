from  typing import List, Optional

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        n = len(nums)

        def dfs(cur):
            if cur == n:
                res.append(path[:])
                return

            path.append(nums[cur])
            dfs(cur + 1)
            path.pop()
            dfs(cur + 1)

        dfs(0)
        return res
