# Binary Tree Right Side View
# Solved
# You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.
#
# Example 1:
#
#
#
# Input: root = [1,2,3]
#
# Output: [1,3]
# Example 2:
#
# Input: root = [1,2,3,4,5,6,7]
#
# Output: [1,3,7]
# Constraints:
#
# 0 <= number of nodes in the tree <= 100
# -100 <= Node.val <= 100
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()

                if i == level_length - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result