from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = deque([(root, 0)])
        max_depth = 0
        total_sum = 0

        while q:
            current_root, current_depth = q.popleft()

            if current_root.left:
                q.append((current_root.left, current_depth + 1))
                max_depth = max(max_depth, current_depth + 1)
                total_sum = 0

            if current_root.right:
                q.append((current_root.right, current_depth + 1))
                max_depth = max(max_depth, current_depth + 1)
                total_sum = 0

            if current_depth == max_depth:
                total_sum += current_root.val

        return total_sum
