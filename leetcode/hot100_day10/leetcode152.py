from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[x, x] for x in nums]
        res = f[0][1]
        for i in range(1, n):
            # 以 i 结尾的子数组乘积的最小值
            if nums[i] >= 0:
                f[i][0] = min(nums[i], f[i - 1][0] * nums[i])
                f[i][1] = max(nums[i], f[i - 1][1] * nums[i])
            else:
                f[i][0] = min(nums[i], f[i - 1][1] * nums[i])
                f[i][1] = max(nums[i], f[i - 1][0] * nums[i])


            res = max(res, f[i][1])

        return res
