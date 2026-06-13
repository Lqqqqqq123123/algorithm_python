from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n
        while l < r:
            mid = l + r >> 1
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l
