'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        if strs:
            s1, s2 = strs[0], strs[-1]
            if s1 is s2:  # same string obj
                return s1

            end, len_m = 0, len(s1)
            while end < len_m and s1[end] == s2[end]:
                end += 1

            return s1[:end]

        return ''