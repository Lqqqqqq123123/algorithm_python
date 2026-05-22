class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if nums[r] >= nums[l]:
            return nums[l]
        x = nums[r]
        while l < r:
            mid = l + r >> 1
            if nums[mid] <= x:
                r = mid
            else:
                l = mid + 1

        return nums[l]