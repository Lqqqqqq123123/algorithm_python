from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n, res = len(nums), []
        nums.sort()

        for i in range(n - 3):
            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, n - 2):
                if j - 1 >= i + 1 and nums[j - 1] == nums[j]:
                    continue

                p, q = j + 1, n - 1
                while p < q:
                    s = nums[i] + nums[j] + nums[p] + nums[q]
                    if s < target:
                        p += 1
                    if s > target:
                        q -= 1
                    if s == target:
                        res.append([nums[i], nums[j], nums[p], nums[q]])
                        # 去重
                        while p + 1 < q and nums[p + 1] == nums[p]:
                            p += 1
                        while q - 1 > p and nums[q - 1] == nums[q]:
                            q -= 1
                        p += 1
                        q -= 1
                
        return res

