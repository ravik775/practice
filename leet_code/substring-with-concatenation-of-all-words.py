"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
Example 1:
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:
Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
"""

from collections import Counter
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        if not (s and words):
            return result
        word_len = len(words[0]) 
        max_len = word_len * len(words)
        index_i, word_cnt, s_len = max_len, Counter(words), len(s)
        temp_c = Counter()
        while index_i <= s_len:
            index_j, index_k = index_i,  index_i - word_len
            s_word = s[index_k: index_j] 
            count_i = word_cnt[s_word]
            temp_c = Counter()
                
            while count_i:
                count_t = temp_c[s_word]
                if count_t == count_i:
                    break
                elif (index_i - index_k) >= max_len:
                    result.append(index_k)
                    break
                else:
                    temp_c[s_word] = count_t + 1
                    index_j, index_k = index_k, index_k - word_len
                    s_word = s[index_k: index_j] 
                    count_i = word_cnt[s_word]
            index_i += 1
        return result