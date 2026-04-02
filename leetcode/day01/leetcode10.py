from PIL.Jpeg2KImagePlugin import BoxReader


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        s = ' ' + s
        p = ' ' + p
        f = [[False] * (m + 10) for _ in range(n + 10)]
        for j in range(m + 1):
            print(j)
            if j == 0:
                f[0][j] = True
            else:
                if p[j] == '*':
                    f[0][j] |= f[0][j - 2]
                else:
                    continue

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j].isalpha() or p[j] == '.':
                    if s[i] == p[j] or p[j] == '.':
                        f[i][j] |= f[i - 1][j - 1]
                elif p[j] == '*':

                    f[i][j] |= f[i][j - 2] # 匹配 0 个
                    # 看看最多能匹配几个
                    t = i
                    while t >= 1 and (s[t] == p[j - 1] or p[j - 1] == '.'):
                        f[i][j] |= f[t - 1][j - 2]
                        t -= 1

        return f[n][m]
if __name__ == '__main__':

    s = Solution()
    print(s.isMatch('aaaa', 'aaaa*'))



