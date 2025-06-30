# Minimum Path Sum
# Solved
# You are given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example 1:
#
# Input: grid = [
#     [1,2,0],
#     [5,4,2],
#     [1,1,3]
# ]
#
# Output: 8
# Explanation: The path with minimum sum is 1 -> 2 -> 0 -> 2 -> 3.
#
# Example 2:
#
# Input: grid = [
#     [2,2],
#     [1,0]
# ]
#
# Output: 3
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])


        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i][j-1],grid[i-1][j])
        return grid[m-1][n-1]