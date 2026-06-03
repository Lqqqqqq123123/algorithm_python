from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f, g = [0] * (n + 1), [0] * (n + 1)
        f[0] = 0; g[0] = -0x3f3f3f3f
        prices = [0] + prices

        res = 0
        for i in range(1, n + 1):
            f[i] = max(f[i - 1], g[i - 1] + prices[i])
            g[i] = max(g[i - 1], f[i - 1] - prices[i])

            res = max(res, f[i])


        return res



