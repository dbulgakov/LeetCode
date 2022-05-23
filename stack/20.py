class Solution:
    def isValid(self, s):
        brackets_map = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for brace in s:
            if brace in brackets_map:
                stack.append(brace)
            elif stack and brackets_map[stack[-1]] == brace:
                stack.pop()
            else:
                return False

        return stack == []