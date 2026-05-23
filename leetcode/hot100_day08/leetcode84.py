from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        heights = [0] + heights + [0]
        ans = 0
        for i in range(0, n + 2):
            while stk and heights[stk[-1]] < heights[i]:
                # 收集答案
                ans = max(ans, heights[stk[-1]] * (i - stk[-2]- 1))
                stk.pop()

            stk.append(i)

        return ans
