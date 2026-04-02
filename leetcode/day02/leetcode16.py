from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res, n, gap = 0, len(nums), float('inf')
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < gap:
                    res = s
                    gap = abs(s - target)

                if s == target:
                    return s
                if s < target:
                    j += 1
                else:
                    k -= 1


        return res


