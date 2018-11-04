"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

e1, m ,e2

  e1 <= k < mid
  
  [5, 1, 3]
   
[1,2,3,4,5,6]
4
stdout
(0, 2, 5, 'c2')
(1, 1, 1, 'c2')
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        e1, e2 = 0, len(nums)-1
        while e1 <= e2:
            mid = (e1 + e2) // 2
            mid_v, left_v, right_v = nums[mid], nums[e1], nums[e2]
            if mid_v == target:
                return mid
            if left_v <= mid_v:
                if left_v <= target < mid_v:
                    e2 = mid - 1
                else:
                    e1 = mid + 1
            else:
                if mid_v < target <= right_v:
                    e1 = mid + 1
                else:
                    e2 = mid - 1

        return -1