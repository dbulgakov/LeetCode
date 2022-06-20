class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                top_left = matrix[top][l + i]

                # bottom left -> top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # bottom right -> bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # top right -> bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # top left -> top right
                matrix[top + i][r] = top_left

            r -= 1
            l += 1
