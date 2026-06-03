from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)

        l, r = 0, n

        def check(x):
            count = 0
            for i in range(n):
                if citations[i] >= x:
                    count += 1

            return count >= x

        while l < r:
            mid = l + r + 1 >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1


        return l
