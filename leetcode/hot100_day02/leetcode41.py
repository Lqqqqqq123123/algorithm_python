from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                k = nums[i]
                nums[k - 1], nums[i] = nums[i], nums[k - 1]

        # print(nums)

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
