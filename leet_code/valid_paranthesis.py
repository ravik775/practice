class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {'(': ')', '[': ']', '{': '}'}
        for symbol in s:
            if symbol in pair:
                stack.append(symbol)
            elif stack and pair[stack[-1]] == symbol:
                del stack[-1]
            else:
                return False

        return not stack

print(Solution().isValid('()'))