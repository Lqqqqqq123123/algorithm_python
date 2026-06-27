from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        f = [0x3f3f3f3f for _ in range(amount + 1)]
        f[0] = 0

        for coin in coins:
            for j in range(coin, amount + 1):
                f[j] = min(f[j], f[j - coin] + 1)

        return -1 if f[amount] == 0x3f3f3f3f else f[amount]
