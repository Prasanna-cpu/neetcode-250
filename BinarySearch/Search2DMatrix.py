# Search a 2D Matrix
# Solved
# You are given an m x n 2-D integer array matrix and an integer target.
#
# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.
#
# Can you write a solution that runs in O(log(m * n)) time?
#
# Example 1:
#
#
#
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
#
# Output: true
# Example 2:
#
#
#
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
#
# Output: false
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10000 <= matrix[i][j], target <= 10000
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False



