from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[0, 0] for _ in range(n + 1)]
        res = 0
        for i in range(1, n + 1):
            f[i][0] = max(f[i-1][0], f[i - 1][1])
            f[i][1] = f[i - 1][0] + nums[i - 1]
            res = max(f[i][0], f[i][1])

        return res