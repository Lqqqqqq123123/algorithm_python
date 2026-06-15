from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        heights = [0] + heights + [0]
        n, res = len(heights), 0

        for i in range(0, n):
            while stk and heights[i] < heights[stk[-1]]:
                cur = stk.pop()
                res = max(res, heights[cur] * (i - stk[-1] - 1))

            stk.append(i)

        return res



