from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        cur, times = nums[0], 0

        while r < n:
            if times == 0 or nums[r] != cur:
                cur = nums[r]
                times = 1
                nums[l] = nums[r]
                l += 1
            elif nums[r] == cur:
                times += 1
                if times <= 2:
                    nums[l] = nums[r]
                    l += 1

            r += 1

        return l + 1



