class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0] * (n + 1)
        f[0] = 1 # 为了计算 f[1] 和 f[2]，f[0] 必须初始化为1
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]


