class Solution:
    def connect(self, root: 'Node', node=None) -> 'Node':
        if not root:
            return None

        root.next = node

        self.connect(root.left, root.right)
        self.connect(root.right, node.left if node else None)

        return root
