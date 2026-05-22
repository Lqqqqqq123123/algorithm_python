from typing import List, Optional

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = l + r >> 1
            if nums[mid] == target:
                return mid

            # 左边有序
            if nums[l] < nums[mid]:
                # target 在左边
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid
            # 右边有序
            if nums[mid] < nums[r]:
                # target 在右边
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid


        return -1
