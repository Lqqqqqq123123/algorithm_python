from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax, rmax = [0] * n, [0] * n
        for i in range(n):
            if i == 0:
                continue
            lmax[i] = max(lmax[i - 1], height[i - 1])

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                continue
            rmax[i] = max(rmax[i + 1], height[i + 1])

        res = 0
        # print(lmax)
        # print(rmax)
        for i in range(n):
            res += max(0, min(lmax[i], rmax[i]) - height[i])

        return res
