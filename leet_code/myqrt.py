"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if 0 <= x < 2 :
            return x
        
        l, h, m = 1, x, x >> 1
        t1 = m ** 2
        t2 = t1 + 2 * m + 1
        
        while not ( t1 <= x < t2) and l < h:
            if t1 > x:
                h = m - 1
            else:
                l = m + 1
            m = (h + l) >> 1
            t1 = m ** 2
            t2 = t1 + 2 * m + 1
        return m
		