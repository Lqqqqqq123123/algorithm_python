from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        l, r = 0, n - 1
        cur = 0
        while cur <= r:
            # print(cur, r)
            while cur <= r and nums[cur] == val:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
            cur += 1
        # print(r + 1)
        # print(nums)
        return r + 1
