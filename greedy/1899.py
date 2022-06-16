class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        res = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for index, value in enumerate(triplet):
                if value == target[index]:
                    res.add(index)

        return len(res) == 3
