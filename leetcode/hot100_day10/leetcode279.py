from cmath import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        # 建模为 完全背包问题，每个物品都可以被用无限次，背包容量为 n
        # 求得的就是恰好装满背包，最小代价，每个物品的代价都是1
        # f[j] 表示容量为 j 的背包，所需要的最小代价
        f = [float('inf') for _ in range(n + 1)]
        f[0] = 0

        # 收集一下物品
        temp = 1
        values = [i * i for i in range(1,(n ** 0.5) + 1)]

        print(values)

        for i in range(1, len(values)):
            # 完全背包问题，正序遍历
            for j in range(values[i], n + 1):
                f[j] = min(f[j], f[j - values[i]] + 1)


        return f[n]
