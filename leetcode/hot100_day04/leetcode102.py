# Definition for a binary tree node.
from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q, res = deque(), []
        # 根节点入队
        q.append(root)

        while q:
            size = len(q)
            layer = []
            while size:
                size -= 1
                front = q.popleft()
                layer.append(front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)

            res.append(layer)

        return res

