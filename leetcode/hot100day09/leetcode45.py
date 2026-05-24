from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        pre_max_len, cur_max_len, res, n = 0, 0, 0, len(nums)

        for i in range(n):
            cur_max_len = max(cur_max_len, i + nums[i])
            if pre_max_len == i:
                res += 1
                pre_max_len = cur_max_len
                cur_max_len = 0

            if pre_max_len >= n - 1:
                return res

        return 0
