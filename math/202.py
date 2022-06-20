from collections import deque


class Solution:
    def isHappy(self, n: int) -> bool:
        q = deque([n])
        seen = set()

        while q:
            number = q.popleft()

            if number in seen:
                return False

            res = 0
            for c in str(number):
                res += int(c) ** 2

            if res == 1:
                return True

            seen.add(number)
            q.append(res)

        return False
