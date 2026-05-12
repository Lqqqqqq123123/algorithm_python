# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(-1, head)

        # 1. 统计节点个数
        temp, n = dummy.next, 0
        while temp: temp = temp.next; n += 1

        # 2. k个一组一组的去反转
        cur = dummy
        while n >= k:
            # 先去保留这k个元素的下一个结点
            times, ne = k + 1, cur
            while times:
                ne = ne.next
                times -= 1
            new_head, old_head = self.reverse_k(cur.next, k)

            # 指针操作
            cur.next = new_head
            old_head.next = ne
            cur = old_head

            n -= k

        return dummy.next




    def reverse_k(self, head, k):
        old_head = head
        cur, p = head, None
        while k:
            ne = cur.next
            cur.next = p; p = cur; cur = ne
            k -= 1

        return p, old_head



