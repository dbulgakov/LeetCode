class Solution:
    def permute(self, nums):
        res = []
        n = len(nums)

        def backtrack(first=0):
            if first == n:
                res.append(nums.copy())

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return res
