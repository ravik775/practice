"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

# '{:b}'.format(int(a, 2) + int(b, 2)) will solve it
"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a, len_b = len(a), len(b)
        if len_a < len_b:
            a, b, len_a, len_b = b, a, len_b, len_a

        # a is larger
        b = '0' * (len_a - len_b) + b

        cal_map = {
            ('0', '0', '0'): ('0', '0'),
            ('0', '0', '1'): ('1', '0'),
            ('0', '1', '0'): ('1', '0'),
            ('1', '0', '0'): ('1', '0'),
            ('0', '1', '1'): ('0', '1'),
            ('1', '1', '0'): ('0', '1'),
            ('1', '0', '1'): ('0', '1'),
            ('1', '1', '0'): ('0', '1'),
            ('1', '1', '1'): ('1', '1'),
        }
        # making a and b of same length
        index, carry, result = len_a - 1, '0', ['0'] * len_a
        while index >= 0:
            result[index], carry = cal_map[(a[index], b[index], carry)]
            index -= 1

        if carry == '1':
            result.insert(0, '1')

        return ''.join(result)
