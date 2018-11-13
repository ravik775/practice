"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # [1,3,1,1,1]
        e1, e2 = 0, len(nums)-1
        while e1 <= e2:
            mid = (e1 + e2) >> 1
            mid_v, left_v, right_v = nums[mid], nums[e1], nums[e2]
            if mid_v == target:
                return True
            if left_v <= mid_v:
                if left_v <= target < mid_v:
                    e2 = mid - 1
                else:
                    while e1 <= e2 and left_v == nums[e1]:
                        e1 = e1 + 1
            else:
                if mid_v < target <= right_v:
                    e1 = mid + 1
                else:
                    while e1 <= e2 and right_v == nums[e2]:
                        e2 = e2 - 1
        return False