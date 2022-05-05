import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.data = nums

    def reset(self) -> List[int]:
        return self.data

    def shuffle(self) -> List[int]:
        data_copy = list(self.data)
        res = []

        while len(data_copy) > 0:
            new_index = random.randint(0, len(data_copy) - 1)
            res.append(data_copy.pop(new_index))

        return res
