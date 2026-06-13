from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n, res = len(nums), []

        l, r = 0, n - 1

        # 第一次出现的位置
        while l < r:
            mid = l + r + 1 >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        res.append(l if nums[l] == target else -1)

        l, r = 0, n - 1
        while l < r:
            mid = l + r + 1 >> 1
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1

        res.append(l if nums[l] == target else -1)

        return res