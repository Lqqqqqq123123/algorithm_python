# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 找倒数第 n + 1 个
        dummy = ListNode(-1, head)
        slow, fast = dummy, dummy
        k = n + 1

        # 1. 快指针先跳 k - 1 步，也就是 n 步
        times = k - 1
        while times:
            fast = fast.next
            times -= 1

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
