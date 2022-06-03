class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        graph_map = {}

        def dfs(node: 'Node'):
            if node in graph_map:
                return graph_map[node]

            node_copy = Node(node.val)
            graph_map[node] = node_copy

            for n in node.neighbors:
                node_copy.neighbors.append(dfs(n))

            return node_copy

        return dfs(node) if node else None
