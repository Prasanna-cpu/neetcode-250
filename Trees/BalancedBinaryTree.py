# Balanced Binary Tree
# Solved
# Given a binary tree, return true if it is height-balanced and false otherwise.
#
# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
# Example 1:
#
#
#
# Input: root = [1,2,3,null,null,4]
#
# Output: true
# Example 2:
#
#
#
# Input: root = [1,2,3,null,null,4,null,5]
#
# Output: false
# Example 3:
#
# Input: root = []
#
# Output: true
# Constraints:
#
# The number of nodes in the tree is in the range [0, 1000].
# -1000 <= Node.val <= 1000
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return True,0  #(is_balanced,height)

            left_balanced,left_height= check(node.left)
            right_balanced,right_height = check(node.right)

            height = 1+max(left_height,right_height)

            balanced = (left_balanced and right_balanced and abs(left_height-right_height)<=1)

            return balanced,height


        return check(root)[0]