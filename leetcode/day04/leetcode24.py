# Definition for singly-linked list.

from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1, head)
        cur = dummy
        while cur.next and cur.next.next:
            p, q, ne = cur.next, cur.next.next, cur.next.next.next

            q.next = p
            p.next = ne
            cur.next = q
            cur = q


        return dummy.next
