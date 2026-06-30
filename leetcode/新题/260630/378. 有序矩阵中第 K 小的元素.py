from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # 思路：二分答案
        # 我们要找的这个答案，是 count(mid) >= k 的最小的 mid
        n = len(matrix)
        def count(x):
            i, j = 0, n - 1
            res = 0
            while i < n and j >= 0:
                if matrix[i][j] <= x:
                    res += j + 1
                    i += 1
                else:
                    j -= 1


            return res


        # 答案值域：matrix[0][0] ~ matrix[n - 1][n - 1]
        l, r = matrix[0][0], matrix[n - 1][n - 1]

        while l < r:
            mid = l + r >> 1
            if count(mid) < k:
                l = mid + 1
            else:
                r = mid

        return l


