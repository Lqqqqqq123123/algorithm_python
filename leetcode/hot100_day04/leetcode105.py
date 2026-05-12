# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i


        def dfs(l1, r1, l2, r2):
            if l1 > r1:
                return None

            # 找到根节点
            root = preorder[l1]
            # 找到根节点在当前中序遍历的位置
            pos = dic[root]

            # 递归处理左子树
            # 左子树的节点数
            size = pos - l2
            left = dfs(l1 + 1, l1 + size, l2, pos - 1)
            right = dfs(l1 + size + 1, r1, pos + 1, r2)

            node = TreeNode(root, left, right)
            return node
        n = len(preorder)
        return dfs(0, n - 1, 0, n - 1)
