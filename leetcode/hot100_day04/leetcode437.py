# Definition for a binary tree node.
from typing import Optional
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sum, cnt, res = 0, defaultdict(int), 0
        cnt[0] = 1
        def dfs(cur):
            if not cur:
                return
            nonlocal res
            nonlocal sum

            sum += cur.val
            need = sum - targetSum
            res += cnt[need]
            cnt[sum] += 1

            dfs(cur.left)
            dfs(cur.right)

            # 回溯
            cnt[sum] -= 1
            sum -= cur.val

        dfs(root)
        return res



