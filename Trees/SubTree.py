# Subtree of Another Tree
# Solved
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
#
# Example 1:
#
#
#
# Input: root = [1,2,3,4,5], subRoot = [2,4,5]
#
# Output: true
# Example 2:
#
#
#
# Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
#
# Output: false
# Constraints:
#
# 0 <= The number of nodes in both trees <= 100.
# -100 <= root.val, subRoot.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
from typing import Optional


class Solution:

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
