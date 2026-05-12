from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 处理一个前缀和数组
        n = len(nums)
        nums = [0] + nums
        s = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + nums[i]

        # 字典来保存 s[l - 1] 出现的次数
        dic = defaultdict(lambda: 0)
        dic[0] = 1
        res = 0
        for i in range(1 , n + 1):
            target = s[i] - k
            res += dic[target]

        return res