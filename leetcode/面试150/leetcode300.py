from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # 直接写 O(nlogn)做法了

        lens = [] # 存储当前长度上升子序列结尾的最小值

        # 1. 从前到后遍历每个数
        for num in nums:
            # 2. 找到 lens 中 >= num 的第一个数
            l, r = 0, len(lens)
            while l < r:
                mid = l + r >> 1
                if lens[mid] < num:
                    l = mid + 1
                else:
                    r = mid


            if len(lens) == 0 or r == len(lens):
                lens.append(num)
            else:
                lens[r] = num

        return len(lens)
