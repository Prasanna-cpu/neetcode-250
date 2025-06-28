# Binary Tree Maximum Path Sum
# Solved
# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Example 1:
#
#
#
# Input: root = [1,2,3]
#
# Output: 6
# Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.
#
# Example 2:
#
#
#
# Input: root = [-15,10,20,null,null,15,5,-5]
#
# Output: 40
# Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.
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
    def __init__(self):
        self.max_sum = None

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        def max_gain(node):
            if not node:
                return 0

            max_left_gain = max(max_gain(node.left),0)
            max_right_gain = max(max_gain(node.right),0)

            current_max_sum = node.val + max_left_gain + max_right_gain

            self.max_sum = max(self.max_sum,current_max_sum)

            return node.val + max(max_left_gain,max_right_gain)

        max_gain(root)
        return self.max_sum
