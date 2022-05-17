from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([(root, 0)])

        res = []

        current_depth = 0

        while q:
            node, depth = q.popleft()

            current_depth = max(current_depth, depth)

            if node.left:
                q.append((node.left, depth + 1))

            if node.right:
                q.append((node.right, depth + 1))

            if not any(q) or q[0][1] > current_depth:
                res.append(node.val)

        return res