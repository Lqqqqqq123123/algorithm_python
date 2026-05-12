from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        pre = nums[0]
        for i in range(1, n):
            res[i] = pre
            pre = pre * nums[i]
        pre = nums[n - 1]
        for i in range(n - 2, -1, -1):
            res[i] = res[i] * pre
            pre = pre * nums[i]

        return res