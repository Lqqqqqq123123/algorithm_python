from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, min_price, res = len(prices), prices[0], 0
        if n == 1:
            return res
        for i in range(1,  n):
            res = max(res, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return res
