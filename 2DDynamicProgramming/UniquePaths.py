# Unique Paths
# Solved
# There is an m x n grid where you are allowed to move either down or to the right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).
#
# You may assume the output will fit in a 32-bit integer.
#
# Example 1:
#
#
#
# Input: m = 3, n = 6
#
# Output: 21
# Example 2:
#
# Input: m = 3, n = 3
#
# Output: 6
# Constraints:
#
# 1 <= m, n <= 100

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]       