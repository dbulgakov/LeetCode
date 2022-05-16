from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        max_depth = 1 if root else 0

        while q:
            element, depth = q.popleft()

            if not element:
                continue

            if element.left or element.right:
                q.append((element.left, depth + 1))
                q.append((element.right, depth + 1))

                max_depth = max(max_depth, depth + 1)

        return max_depth
