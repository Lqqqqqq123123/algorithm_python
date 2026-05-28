from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 快慢指针先相遇
        slow, fast = 0, 0
        head = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while head != slow:
                    head = nums[head]
                    slow = nums[slow]

                return head

        return -1





