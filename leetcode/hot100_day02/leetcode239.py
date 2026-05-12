from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxq, res = deque(), []
        n = len(nums)
        for i in range(n):
            # 删除过期的元素
            while maxq and i - maxq[0] + 1 > k:
                maxq.popleft()

            # 删除没用的元素
            while maxq and nums[maxq[-1]] <= nums[i]:
                maxq.pop()

            maxq.append(i)
            if i >= k - 1:
                res.append(nums[maxq[0]])


        return res
