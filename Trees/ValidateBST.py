# Valid Binary Search Tree
# Solved
# Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.
#
# A valid binary search tree satisfies the following constraints:
#
# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.
# Example 1:
#
#
#
# Input: root = [2,1,3]
#
# Output: true
# Example 2:
#
#
#
# Input: root = [1,2,3]
#
# Output: false
# Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.
#
# Constraints:
#
# 1 <= The number of nodes in the tree <= 1000.
# -1000 <= Node.val <= 1000
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def depth_first_search(node, min_val, max_val):
            if not node:
                return True

            if not (min_val < node.val < max_val):
                return False

            return (
                    depth_first_search(node.left, min_val, node.val) and
                    depth_first_search(node.right, node.val, max_val)
            )

        MAX_VAL = float("inf")
        MIN_VAL = float("-inf")
        return depth_first_search(root, MIN_VAL, MAX_VAL)