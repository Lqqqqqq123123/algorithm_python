from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 无论怎么旋转，切一刀左右两边一定又一边是有序的，
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = l + r  >> 1
            if nums[mid] == target:
                return mid
            # 左边有序
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1


        return -1