# Construct Binary Tree from Preorder and Inorder Traversal
# Solved
# You are given two integer arrays preorder and inorder.
#
# preorder is the preorder traversal of a binary tree
# inorder is the inorder traversal of the same tree
# Both arrays are of the same size and consist of unique values.
# Rebuild the binary tree from the preorder and inorder traversals and return its root.
#
# Example 1:
#
#
#
# Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
#
# Output: [1,2,3,null,null,null,4]
# Example 2:
#
# Input: preorder = [1], inorder = [1]
#
# Output: [1]
# Constraints:
#
# 1 <= inorder.length <= 1000.
# inorder.length == preorder.length
# -1000 <= preorder[i], inorder[i] <= 1000

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root_index = inorder.index(root_val)

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]

        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]

        left_child = self.buildTree(left_preorder,left_inorder)
        right_child = self.buildTree(right_preorder,right_inorder)

        return TreeNode(root_val,left_child,right_child)  
