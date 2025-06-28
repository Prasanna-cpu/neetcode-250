# Longest Increasing Path in Matrix
# Solved
# You are given a 2-D grid of integers matrix, where each integer is greater than or equal to 0.
#
# Return the length of the longest strictly increasing path within matrix.
#
# From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.
#
# Example 1:
#
#
#
# Input: matrix = [[5,5,3],[2,3,6],[1,1,1]]
#
# Output: 4
# Explanation: The longest increasing path is [1, 2, 3, 6] or [1, 2, 3, 5].
#
# Example 2:
#
#
#
# Input: matrix = [[1,2,3],[2,1,4],[7,6,5]]
#
# Output: 7
# Explanation: The longest increasing path is [1, 2, 3, 4, 5, 6, 7].
#
# Constraints:
#
# 1 <= matrix.length, matrix[i].length <= 100
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]  # stores only length strictly

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            max_path = 1

            if dp[r][c] != 0:
                return dp[r][c]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(nr, nc))
            dp[r][c] = max_path
            return max_path

        max_length = 0

        for r in range(rows):
            for c in range(cols):
                max_length = max(max_length, dfs(r, c))

        return max_length