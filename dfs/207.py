from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def dfs(course: int):
            if course in visited:
                return False
            if not preMap[course]:
                return True

            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
