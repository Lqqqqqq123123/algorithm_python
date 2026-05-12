# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, _root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            dfs(root.left)
            root.left = None
            nonlocal pre
            root.right = pre
            pre = root

        dfs(_root)
        


