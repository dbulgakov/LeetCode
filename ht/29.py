class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        comb_n = 2 ** k
        seen_combinations = set()

        for i in range(0, len(s) - 1):
            seen_combinations.add(s[i:i + 2])

        return comb_n == seen_combinations
