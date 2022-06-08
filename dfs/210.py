from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycle, visit = set(), set()
        res = []

        def dfs(course: int):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
