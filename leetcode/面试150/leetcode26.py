from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while r < n:
            if r >= 1 and nums[r] != nums[r - 1]:
                nums[l] = nums[r - 1]
                l += 1

            r += 1

        nums[l] = nums[n - 1]

        