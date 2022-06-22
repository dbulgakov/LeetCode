from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(r: Optional[TreeNode]) -> int:
            if not r:
                return 0

            left = dfs(r.left)
            right = dfs(r.right)

            leftMax = max(left, 0)
            rightMax = max(right, 0)

            self.res = max(self.res, r.val + leftMax + rightMax)

            return r.val + max(leftMax, rightMax)

        dfs(root)

        return self.res
