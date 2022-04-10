class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters_dict = dict()
        start_index = 0
        max_length = 0

        for index, letter in enumerate(s):
            if letter in letters_dict:
                start_index = max(letters_dict[letter] + 1, start_index)

            max_length = max(max_length, (index - start_index) + 1)
            letters_dict[letter] = index

        return max_length
