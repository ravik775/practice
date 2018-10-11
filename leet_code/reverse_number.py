"""


"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        nsign = x < 0
        if nsign:
            x = ~x + 1

        rnum = 0
        while x:
            rnum = rnum * 10 + x % 10
            x = x // 10

        if rnum < 0 or rnum >= (2 ** 31 - 1):
            return 0

        return ~rnum + 1 if nsign else rnum
