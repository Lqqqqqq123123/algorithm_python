# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(cur):
            if not cur:
                return 0

            l = dfs(cur.left)
            r = dfs(cur.right)
            nonlocal res
            # 1.
            res = max(res, max(cur.val, cur.val + max(0, l) + max(0, r)))

            return max(cur.val + max(0, l), cur.val + max(0, r))


        dfs(root)
        return res


