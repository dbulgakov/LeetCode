from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: int(x / y)}

        stack = []

        for t in tokens:
            if t in op:
                first_number = stack.pop()
                second_number = stack.pop()
                operation_result = op[t](second_number, first_number)

                stack.append(operation_result)
            else:
                stack.append(int(t))

        return stack[0]
