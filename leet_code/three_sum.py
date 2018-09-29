
'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import bisect
        nums.sort()
        result, nums_len, index_i, prev_value_a = [], len(nums), 0, None
        a_max, b_max = nums_len - 2, nums_len - 1
        while (index_i < a_max):
            value_a = nums[index_i]
            index_i += 1
            if prev_value_a != value_a:
                if value_a > 0:  # while there are negative and positie numbers
                    break
                prev_value_a, prev_value_b, index_j, value_a_negative = value_a, None, index_i, -1 * value_a

                while index_j < b_max:
                    value_b = nums[index_j]
                    index_j += 1
                    if prev_value_b != value_b:
                        if value_b > value_a_negative:
                            break
                        prev_value_b, value_c_to_find = value_b, -1 * (value_a + value_b)
                        indx = bisect.bisect_left(nums, value_c_to_find, index_j)
                        if indx < nums_len and nums[indx] == value_c_to_find:
                            result.append([value_a, value_b, value_c_to_find])

        return result
