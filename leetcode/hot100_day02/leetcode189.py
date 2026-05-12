from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, st, ed):
            while st < ed:
                arr[st], arr[ed] = arr[ed], arr[st]
                st += 1
                ed -= 1

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)

        
