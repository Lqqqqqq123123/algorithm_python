# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy

        t = 0 # 进位
        while l1 or l2:
            if l1:
                t += l1.val; l1 = l1.next
            if l2:
                t += l2.val; l2 = l2.next

            cur.next = ListNode(t % 10)
            t //= 10
            cur = cur.next

        if t:
            cur.next = ListNode(1)

        return dummy.next



