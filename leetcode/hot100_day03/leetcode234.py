# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return True

        # 1. 快慢指针找中点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 反转后半部分
        temp = slow.next
        slow.next = None
        new_head = self.reverse(temp)

        # 3. 比较
        while head and new_head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next


        return True

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            ne = cur.next
            cur.next = pre; pre = cur; cur = ne
        return pre

