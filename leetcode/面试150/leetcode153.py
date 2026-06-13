from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        if nums[0] <= nums[n - 1]:
            return nums[0]
        # 二分答案
        l, r = 0, n - 1
        x = nums[r]
        while l < r:
            mid = l + r >> 1
            if nums[mid] > x:
                l = mid + 1
            else:
                r = mid

        return nums[l]

