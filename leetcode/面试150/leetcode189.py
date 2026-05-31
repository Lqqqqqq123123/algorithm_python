from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路2：向右轮转 k 个
        n = len(nums)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1


        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        