from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, j, idx = 0, 0, 0
        for t in range(n * m):
            # print(i, j)
            res.append(matrix[i][j])
            matrix[i][j] = 666

            nx, ny = i + directions[idx][0], j + directions[idx][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or matrix[nx][ny] == 666:
                idx = (idx + 1) % 4
                nx, ny = i + directions[idx][0], j + directions[idx][1]
                # print(nx, ny)

            i, j = nx, ny

        return res
