class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow_wrapper(x: float, n: int) -> float:
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = pow_wrapper(x, n // 2)
            res = res * res

            return x * res if n % 2 == 1 else res

        res = pow_wrapper(x, abs(n))

        return res if n >= 0 else 1 / res
