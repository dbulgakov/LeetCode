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

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        covered: set[Optional[TreeNode]] = {None}

        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode] = None) -> int:
            if not node:
                return 0

            dfs(node.left, node)
            dfs(node.right, node)

            if (parent is None and node not in covered) or node.left not in covered or node.right not in covered:
                self.res += 1
                covered.add(node)
                covered.add(parent)
                covered.add(node.left)
                covered.add(node.right)

        dfs(root)

        return self.res
