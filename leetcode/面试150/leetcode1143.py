from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        text1 = " " + text1
        text2 = " " + text2
        f = [[0] * (m + 10) for _ in range(n + 10)]

        # f[i][j] 1 - n 和 1 - j 的最长子序列是多少
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i] == text2[j]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])

        return f[n][m]

