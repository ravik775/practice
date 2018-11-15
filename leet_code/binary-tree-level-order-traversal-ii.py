"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return result

        append_to_result = result.append
        queue = [root]
        while queue:
            queue2, data = [], []
            append_to_queue = queue2.append
            add_to_data = data.append
            for node in queue:
                add_to_data(node.val)
                if node.left is not None:
                    append_to_queue(node.left)
                if node.right is not None:
                    append_to_queue(node.right)
            append_to_result(data)
            queue = queue2
        
        result.reverse()
        return result
                
                