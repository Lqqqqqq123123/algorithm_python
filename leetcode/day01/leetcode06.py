class Solution:
    def convert(self, s: str, numRows: int) -> str:
        g = [[] for _ in range(numRows)]
        dir = [i for i in range(numRows)] + [i for i in range(numRows - 2, 0, -1)]
        n = len(dir)
        idx = 0

        for c in s:
            g[dir[idx]].append(c)
            idx = (idx + 1) % n
        res = ''
        for i in range(numRows):
            res += ''.join(g[i])

        return res










