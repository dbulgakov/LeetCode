from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(r: Optional[TreeNode]) -> int:
            if not r:
                return -1

            left = dfs(r.left)
            right = dfs(r.right)

            if abs(right - left) > 1:
                self.ans = False

            return 1 + max(left, right)

        dfs(root)

        return self.ans
