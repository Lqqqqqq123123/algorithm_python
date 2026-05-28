from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur, times = 0, 0
        for num in nums:
            if times == 0:
                cur = num
            else:
                if cur == num:
                    times += 1
                else:
                    times -= 1

        return cur
