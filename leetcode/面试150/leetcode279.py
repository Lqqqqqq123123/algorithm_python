from cmath import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        # 建模为 完全背包问题，每个物品都可以被用无限次，背包容量为 n
        # 求得的就是恰好装满背包，最小代价，每个物品的代价都是1
        # f[j] 表示容量为 j 的背包，所需要的最小代价
        f = [float('inf') for _ in range(n + 1)]
        f[0] = 0

        # 收集一下物品
        values = [i * i for i in range(1, int(n ** 0.5) + 1)]

        print(values)

        # 完全背包问题
        # 遍历每一件物品
        for v in values:
            # 遍历背包容量
            for j in range(v, n + 1):
                f[j] = max(f[j], f[j - v] + 1)

        return f[n]


if __name__ == '__main__':
    Solution().numSquares(10)
