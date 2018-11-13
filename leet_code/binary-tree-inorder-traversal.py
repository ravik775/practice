"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        left_pro = []
        result = []
        cn = root
        while cn:
            while cn.left:
                left_pro.append(cn)
                cn = cn.left
            
            #only right node or leaf node
            result.append(cn.val)
            cn = cn.right
            while cn is None and left_pro:
                cn = left_pro.pop()
                result.append(cn.val)
                cn = cn.right
        return result