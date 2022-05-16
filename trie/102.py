# Definition for a binary tree node.
from collections import deque, defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])

        res = defaultdict(list)

        while q:
            node, depth = q.popleft()

            if node.left:
                q.append((node.left, depth + 1))

            if node.right:
                q.append((node.right, depth + 1))

            res[depth].append(node.val)

        return list(res.values())
