from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        n = len(nums)
        for i in range(n):
            x = target - nums[i]
            if x in dic:
                return [dic[x], i]
            dic[nums[i]] = i
        return  []