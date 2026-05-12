from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur, pre = head, None
        while cur:
            ne = cur.next
            cur.next = pre; pre = cur; cur = ne

        return pre
