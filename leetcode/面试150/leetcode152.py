from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        # f[i][0] 表示以 i 结尾的子数组乘积的最小值
        # f[i][1] 表示以 i 结尾的子数组乘积的最大值

        f = [[x, x] for x in nums]
        res = f[0][1]

        for i in range(1, n):
            if nums[i] > 0:
                f[i][0] = min(f[i - 1][0] * nums[i], nums[i])
                f[i][1] = max(f[i - 1][1] * nums[i], nums[i])
            else:
                f[i][1] = min(nums[i], f[i - 1][0] * nums[i])
                f[i][0] = max(nums[i], f[i - 1][1] * nums[i])

            res = max(res, f[i][1])

        return res