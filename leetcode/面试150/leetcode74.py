from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        # 思路：把二维矩阵映射为 1d
        l, r = 0, n * m - 1
        while l <= r:
            mid = l +r >> 1
            x, y = mid // m, mid % m
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False