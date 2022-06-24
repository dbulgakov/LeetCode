class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        ps_pairs = [(p, s) for p, s in zip(position, speed)]

        stack = []

        for pos, speed in reversed(sorted(ps_pairs)):
            stack.append((target - pos) / speed)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
