# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 递归排序
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 1. 找到中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next= None

        left = self.sortList(head)
        right = self.sortList(mid)

        # 2. 二路归并
        dummy = ListNode(-1)
        cur = dummy
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next

            cur = cur.next

        if left:
            cur.next = left
        if right:
            cur.next = right

        return dummy.next
