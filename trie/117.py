from collections import deque
from typing import Optional


class Solution:
    def connect(self, root: Optional['Node']) -> Optional['Node']:

        if not root:
            return root

        q = deque([root])

        while q:
            size = len(q)

            for i in range(size):

                node = q.popleft()

                if i < size - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
