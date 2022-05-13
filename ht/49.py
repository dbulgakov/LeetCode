from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            anagrams = res_dict.get(sorted_s, [])
            anagrams.append(s)
            res_dict[sorted_s] = anagrams

        return list(res_dict.values())
