from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [i for i in nums]
        res = f[0]
        for i in range(1, n):
            f[i] = max(f[i - 1] + nums[i], nums[i])
            res = max(res, f[i])

        return res