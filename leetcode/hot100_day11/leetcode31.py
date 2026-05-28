from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 从后往前找，找到第一个非递增的数
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break

            i -= 1
        # 当前这个序列已经是最大的了
        if i < 0:
            return nums.reverse()

        # 倒着找，找到第一个比nums[i]大的数
        j = n - 1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1

        # 交换
        nums[i], nums[j] = nums[j], nums[i]
        # 反转
        nums[i + 1:] = nums[i + 1:][::-1]




