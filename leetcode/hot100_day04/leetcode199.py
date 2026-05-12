# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import List, Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, q = [], deque()

        q.append(root)

        while q:
            size = len(q)
            while size:
                size -= 1
                cur = q.popleft()
                if not size:
                    res.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return res



