'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        holder = [''] * n * 2

        def gen_p(open_c, end_c):
            index = open_c + end_c
            if open_c > end_c:
                holder[index] = ')'
                gen_p(open_c, end_c + 1)
            elif end_c == n:
                result.append(''.join(holder))

            if open_c < n:
                holder[index] = '('
                gen_p(open_c + 1, end_c)

        gen_p(0, 0)
        return result