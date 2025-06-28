# Diameter of Binary Tree
# Solved
# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.
#
# The length of a path between two nodes in a binary tree is the number of edges between the nodes.
#
# Given the root of a binary tree root, return the diameter of the tree.
#
# Example 1:
#
#
#
# Input: root = [1,null,2,3,4,5]
#
# Output: 3
# Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].
#
# Example 2:
#
# Input: root = [1,2,3]
#
# Output: 2
# Constraints:
#
# 1 <= number of nodes in the tree <= 100
# -100 <= Node.val <= 100
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_dim = None

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dim = 0

        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            self.max_dim = max(self.max_dim, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return self.max_dim

