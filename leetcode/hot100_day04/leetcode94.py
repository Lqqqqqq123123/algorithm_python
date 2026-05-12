# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 非递归写法，就是用栈去模拟递归过程
        stk, res = [], []

        while root or stk:
            while root:
                stk.append(root)
                root = root.left


            root = stk.pop()
            res.append(root.val)
            root = root.right

        return res


