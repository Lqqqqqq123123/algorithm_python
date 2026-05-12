# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(-1, head)

        # 统计当前节点个数
        cur = dummy.next
        n = 0
        while cur:
            n += 1
            cur = cur.next

        cur = dummy

        while n >= k:
            # 先找到这k个节点的下个节点
            ne, times = cur, k + 1
            while times:
                times -= 1
                ne = ne.next

            # 原来的头节点
            old_head = cur.next
            new_head = self.reverse(cur.next, k)
            cur.next = new_head
            old_head.next = ne
            cur = old_head
            n -= k

        return dummy.next


    def reverse(self, head, k):
        cur, p = head, None
        while k:
            k -= 1
            ne = cur.next
            cur.next = p
            p = cur; cur = ne

        return p