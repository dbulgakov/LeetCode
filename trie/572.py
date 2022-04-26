class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False

            return s.val == t.val and dfs(s.left, t.left) and dfs(s.right, t.right)

        if not s:
            return False

        if s.val == t.val and dfs(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
