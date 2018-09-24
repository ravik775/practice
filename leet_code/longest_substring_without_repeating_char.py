
'''
Given a string, find the length of the longest substring without repeating characters.
Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}
        start, max_len = 0, 0
        for ind, elem in enumerate(s):
            p_ind = cache.get(elem, -1)
            if p_ind >= start:
                # found a duplicate char
                max_len = max(ind-start, max_len)
                start = p_ind + 1
            cache[elem] = ind
        max_len = max(max_len, len(s)-start)
        return max_len