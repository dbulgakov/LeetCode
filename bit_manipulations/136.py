class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a


s = Solution()

s.singleNumber([4, 1, 2, 1, 2])
