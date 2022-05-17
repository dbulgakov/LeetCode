# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque([(root, float('-inf'))])
        res = 0

        while q:
            node, path_max = q.popleft()

            if node.val >= path_max:
                res += 1

            if node.left:
                q.append((node.left, max(node.val, path_max)))

            if node.right:
                q.append((node.right, max(node.val, path_max)))

        return res
