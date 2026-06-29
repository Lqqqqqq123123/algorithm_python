from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0
        head = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]

            while head != slow:
                head = nums[head]
                slow = nums[slow]


        return head
