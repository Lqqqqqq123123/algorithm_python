from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, max_pos = len(nums), 0
        for i in range(n):
            if i > max_pos:
                return False
            max_pos = max(max_pos, i + nums[i])
            if max_pos >= n - 1:
                return True

        return False
