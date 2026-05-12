from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:return 0

        s = set(nums)
        res = 1
        for x in s:
            if x - 1 in s:
                continue
            k, cur = 1, x + 1
            while cur in s:
                cur += 1
                k += 1
            res = max(res, k)


        return res