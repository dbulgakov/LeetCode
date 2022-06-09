class Solution:
    def reverse(self, x):
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = int("-{0}".format(str(x)[:0:-1]))

        if result.bit_length() < 32:
            return result

        return 0
