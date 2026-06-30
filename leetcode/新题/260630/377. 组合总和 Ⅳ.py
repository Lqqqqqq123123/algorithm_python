from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 思路：完全背包问题，但是要注意，此时求的是排列数，不是组合数

        # 所以和传统的完全背包问题不同，当前需要先遍历容量，在遍历物品

        f = [0] * (target + 1)
        f[0] = 1
        for j in range(1, target + 1):
            for v in nums:
                if j >= v:
                    f[j] += f[j - v]

        return f[target]


