class Solution:
    # Time: O(n)
    # Space: O(n)

    def partitionLabels(self, s: str) -> list[int]:
        letter_dict = {}

        for index, letter in enumerate(s):
            letter_dict[letter] = index

        res = []
        size, end = 0, letter_dict[s[0]]

        for index, letter in enumerate(s):
            size += 1
            end = max(end, letter_dict[letter])

            if index == end:
                res.append(size)
                size = 0

        return res
