class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        len_n, len_h = len(needle), len(haystack)

        if len_n <= len_h:
            start = len_n
            while start <= len_h:
                ind1, ind2 = len_n - 1, start - 1
                while ind1 >= 0 and needle[ind1] == haystack[ind2]:
                    ind1 -= 1
                    ind2 -= 1
                if ind1 < 0:
                    return ind2 + 1
                start += 1
        return -1

print(Solution().strStr("a", 'a'))