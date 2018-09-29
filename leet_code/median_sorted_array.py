'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        n_elems = len1 + len2
        if n_elems & 1:
            k_elem_ind = (n_elems // 2)
        else:
            k_elem_ind = (n_elems - 1) // 2
        k_val, k_val_next = None, None
        k_elem_ind += 1
        index1, index2, k_index = 0, 0, 0

        while index1 < len1 and index2 < len2 and k_index <= k_elem_ind:
            k_val = k_val_next
            a, b = nums1[index1], nums2[index2]
            if a <= b:
                k_val_next = a
                index1 += 1
            else:
                k_val_next = b
                index2 += 1
            k_index += 1

        if index1 == len1:
            index_left, len_left, nums_left = index2, len2, nums2
        else:
            index_left, len_left, nums_left = index2, len2, nums2

        # still we are not found k_val
        while index_left < len_left and k_index <= k_elem_ind:
            k_val, k_val_next = k_val_next, nums_left[index_left]
            index_left, k_index = index_left + 1, k_index + 1

        if n_elems & 1:
            return k_val or k_val_next
        return (k_val + k_val_next) / 2.0

print(Solution().findMedianSortedArrays([], [3,4]))