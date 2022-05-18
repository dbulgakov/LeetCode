import math
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], left_boundry: int, right_boundry: int):
            if not node:
                return True

            if not left_boundry < node.val < right_boundry:
                return False

            return valid(node.left, left_boundry, node.val) and valid(node.right, node.val, right_boundry)

        return valid(root, -math.inf, math.inf)
