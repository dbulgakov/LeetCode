from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        check_map = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        res = []

        def backtrack(combination: str):
            index = len(combination)

            if index == len(digits):
                res.append(combination)
                return

            for i in check_map[int(digits[index])]:
                backtrack(combination + i)

        if len(digits) > 0:
            backtrack('')

        return res
