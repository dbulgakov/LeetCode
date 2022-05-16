# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(r: Optional[TreeNode]):
            if not root:
                return

            r.left, r.right = r.right, r.left
            invert(r.left)
            invert(r.right)

        invert(root)
        return root
