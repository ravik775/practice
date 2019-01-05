"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        dummy = TreeNode(0)
        q2 = [(0, len(nums)-1, dummy, 1)]
        while q2:
            l, h, root, side = q2.pop()
            if l <= h:
                m = (l+h) >> 1
                nNode = TreeNode(nums[m])
                if side:
                    root.right = nNode
                else:
                    root.left = nNode
                q2.append((l, m-1, nNode, 0))
                q2.append((m+1, h, nNode, 1))
        return dummy.right