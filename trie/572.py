from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True

            if not p or not q or p.val != q.val:
                return False

            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        if not s:
            return False

        if s.val == t.val and is_same_tree(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
