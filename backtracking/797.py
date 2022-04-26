from typing import List, Any


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n_elements = len(graph) - 1

        def backtrack(i, arr):
            if i == n_elements:
                res.append(arr.copy())
                return

            for node in graph[i]:
                arr.append(node)
                backtrack(node, arr)
                arr.pop()

        backtrack(0, [0])

        return res
