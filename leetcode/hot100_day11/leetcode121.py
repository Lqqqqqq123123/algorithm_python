class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_price, res, n = prices[0], 0, len(prices)
        for i in range(1, n):
            res = max(res, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return res

