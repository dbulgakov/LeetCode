class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        letter_dict = {}
        for l in s:
            letter_dict[l] = letter_dict.get(l, 0) + 1

        v = letter_dict.popitem()[1]

        for k, val in letter_dict.items():
            if v != val:
                return False
        return True
