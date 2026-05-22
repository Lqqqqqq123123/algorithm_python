from typing import List, Optional

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        l, r = 0, n - 1
        res = []
        if n == 0:
            return res
        while l < r:
            mid = l + r >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1


        res.append(-1) if nums[l] != target else res.append(l)

        l, r = 0, n - 1

        while l < r:
            mid = l + r + 1 >> 1
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1

        res.append(-1) if nums[r] != target else res.append(r)

        return res