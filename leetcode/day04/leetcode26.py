from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 0

        while i < n:
            if nums[i] == nums[j]:
                i += 1
            else:
                nums[j + 1] = nums[i]
                j += 1

        return j + 1
