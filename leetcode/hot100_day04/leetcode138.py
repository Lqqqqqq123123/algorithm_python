from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1. 先去复制所有结点
        dic:dict[Node|None, Node|None] = {None: None}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next

        # 2. 再去复制边
        cur = head
        while cur:
            dic[cur].next = dic[cur.next]
            dic[cur].random = dic[cur.random]
            cur = cur.next

        return dic[head]