# Definition for singly-linked list.
from typing import List, Optional, TypedDict
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ListNode.__lt__ = lambda x, y: x.val < y.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for lis in lists:
            if lis:
                heapq.heappush(heap, lis)


        # 虚拟节点
        dummy = ListNode(-1)
        cur = dummy
        while heap:
            top = heapq.heappop(heap)
            cur.next = top
            cur = cur.next

            if top.next:
                heapq.heappush(heap, top.next)

        return dummy.next
