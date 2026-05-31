from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 思路：一换一算法
        cur, times = 0, 0
        for num in nums:
            if times == 0:
                cur = num
                times = 1
            else:
                if num == cur:
                    times += 1
                else:
                    times -= 1

        return cur
