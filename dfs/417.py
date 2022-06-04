from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific: set[(int, int)] = set()
        atlantic: set[(int, int)] = set()

        def dfs(i: int, j: int, prevHeight: int, ocean: set[(int, int)]) -> None:
            if (i, j) in ocean \
                    or not (0 <= i < len(heights) and 0 <= j < len(heights[0])) \
                    or heights[i][j] < prevHeight:
                return

            ocean.add((i, j))

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + di, j + dj, heights[i][j], ocean)

        for i in range(0, len(heights[0])):
            dfs(0, i, heights[0][i], pacific)
            dfs(len(heights) - 1, i, heights[len(heights) - 1][i], atlantic)

        for j in range(0, len(heights)):
            dfs(j, 0, heights[j][0], pacific)
            dfs(j, len(heights[0]) - 1, heights[j][len(heights[0]) - 1], atlantic)

        return list(pacific.intersection(atlantic))
