from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row_count = len(image)
        col_count = len(image[0])

        check_color = image[sr][sc]

        if newColor == check_color:
            return image

        def bfs(row, col):
            if image[row][col] == check_color:
                image[row][col] = newColor

                if row >= 1:
                    bfs(row - 1, col)
                if row + 1 < row_count:
                    bfs(row + 1, col)
                if col >= 1:
                    bfs(row, col - 1)
                if col + 1 < col_count:
                    bfs(row, col + 1)

        bfs(sr, sc)
        return image