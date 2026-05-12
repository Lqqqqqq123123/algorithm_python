# Definition for singly-linked list.
from typing import Optional, List
import heapq

from sympy.physics.units import kat


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ListNode.__lt__ = lambda x, y: x.val < y.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # 小根堆
        heap, n = [], len(lists)
        for i in range(n):
            cur = lists[i]
            if cur:
                heapq.heappush(heap, cur)

        # 多路归并
        dummy = ListNode(-1)
        tail = dummy
        while heap:
            cur = heapq.heappop(heap)
            tail.next = cur
            tail = tail.next

            if cur.next:
                heapq.heappush(heap, cur.next)


        return dummy.next





