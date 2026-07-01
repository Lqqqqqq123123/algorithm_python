import random
from typing import List

random.shuffle
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.backup = self.nums.copy() # 浅拷贝够用了


    def reset(self) -> List[int]:
        return self.backup.copy()

    def shuffle(self) -> List[int]:
        # Fisher-Yates 洗牌算法
        for i in range(len(self.nums) - 1, 0, -1):
            j = random.randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()