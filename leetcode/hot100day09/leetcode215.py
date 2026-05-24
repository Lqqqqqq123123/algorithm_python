from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 第 k 大个数，就是 n - k + 1 小的数
        # 快排去找第 k 小的数
        def dfs(l, r, t) -> int:
            if l >= r:
                return nums[l]
            i, j, pivot = l - 1, r + 1, nums[l + r >> 1]
            while i < j:
                i, j = i + 1, j - 1
                while nums[i] < pivot: i += 1
                while nums[j] > pivot: j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]

            if j - l + 1 >= t:
                return dfs(l, j, t)
            else:
                return dfs(j + 1, r, t - (j - l  + 1))

        return dfs(0, len(nums) - 1, len(nums) - k + 1)
