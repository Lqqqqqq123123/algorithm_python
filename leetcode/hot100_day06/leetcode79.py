from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        n, m = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word) - 1:
                return True
            board[i][j] = '#'
            for dx, dy in dir:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and board[x][y] == word[k + 1]:
                    if dfs(x, y, k + 1):
                        return True

            board[i][j] = word[k]
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False
