from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False

        f = [False] * (s // 2 + 1)
        f[0] = True

        # 做个 0, 1 背包
        for num in nums:
            for i in range(s // 2, num - 1, -1):
                f[i] = f[i] or f[i - num]


        return f[s // 2]
