from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 最长递增子序列
        # 做法 1，dp O(n2)
        # 做法 2，贪心 O(logn)

        lens, n = [], len(nums)
        for i in range(n):
            if not lens:
                lens.append(nums[i])
                continue
            # 二分出 >= 这个数的位置
            l, r = 0, len(lens) - 1
            while l < r:
                mid = l + r >> 1
                if lens[mid] < nums[i]:
                    l = mid + 1
                else:
                    r = mid



            if not lens or lens[l] < nums[i]:
                lens.append(nums[i])
            else:
                lens[l] = nums[i]

        return len(lens)
