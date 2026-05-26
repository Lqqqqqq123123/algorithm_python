from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 建模为 0,1 背包问题
        half = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False

        n, f = len(nums), [False] * (half)
        f[0] = True

        for value in nums:
            for j in range(half, value - 1, -1):
                f[j] |= f[j - value]


        return f[half]
    


