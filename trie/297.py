from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.index = 0

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(r: Optional[TreeNode]) -> None:
            if not r:
                res.append('N')
                return

            res.append(str(r.val))
            dfs(r.left)
            dfs(r.right)

        dfs(root)
        return ','.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        self.index = 0

        def dfs():
            if vals[self.index] == 'N':
                self.index += 1
                return None

            node = TreeNode(int(vals[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
