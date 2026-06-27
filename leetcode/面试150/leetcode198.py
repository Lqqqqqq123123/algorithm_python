from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        # 定义状态： f[i][0]: 1-i天且i天不偷窃，f[i][1]: 1-i天且i天偷窃
        n = len(nums)
        f = [[0, 0] for _ in range(n + 1)]
        # 初态
        f[0][1] = nums[0]

        # dp
        res = f[0][1]
        for i in range(1, n):
            # 不偷窃
            f[i][0] = max(f[i - 1][0], f[i - 1][1])
            # 偷窃
            f[i][1] = f[i - 1][0] + nums[i]

            res = max(f[i][0], f[i][1])


        return res




