# Definition for singly-linked list.

from typing import Optional
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.arr = []

        while head:
            self.arr.append(self.head.val)
            self.head = head.next

    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()