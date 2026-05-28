class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        word1, word2 = ' ' + word1, ' ' + word2

        f = [[float('inf')] * (m + 10) for _ in range(n + 10)]

        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i == 0:
                    f[i][j] = j
                if j == 0:
                    f[i][j] = i
                else:
                    if word1[i] == word2[j]:
                        f[i][j] = f[i - 1][j - 1]
                    else:
                        f[i][j] = min(f[i - 1][j], min(f[i][j - 1], f[i - 1][j - 1])) + 1

        return f[n][m]

