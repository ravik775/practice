"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

import bisect
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums and (nums[0] <= target <= nums[-1]):
            ind = bisect.bisect_left(nums, target)
            #print ('got %s at ind %s'%(target, ind))
            if nums[ind] == target:
                return [ ind, bisect.bisect_right(nums, target)-1]
        return [-1, -1]