# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(r: Optional[TreeNode]) -> int:
            if not r:
                return -1

            left = dfs(r.left)
            right = dfs(r.right)

            d = 2 + left + right

            self.res = max(self.res, d)

            return 1 + max(left, right)

        dfs(root)

        return self.res
