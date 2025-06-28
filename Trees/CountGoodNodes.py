class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):

            if not node:
                return 0

            if node.val >= max_so_far:
                good = 1
            else:
                good = 0

            max_so_far = max(max_so_far, node.val)

            good += dfs(node.left, max_so_far)
            good += dfs(node.right, max_so_far)

            return good

        return dfs(root, root.val)

    