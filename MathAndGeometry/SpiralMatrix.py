# Spiral Matrix
# Solved
# Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.
#
# Example 1:
#
#
#
# Input: matrix = [[1,2],[3,4]]
#
# Output: [1,2,4,3]
# Example 2:
#
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#
# Output: [1,2,3,6,9,8,7,4,5]
# Example 3:
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# Constraints:
#
# 1 <= matrix.length, matrix[i].length <= 10
# -100 <= matrix[i][j] <= 100
#
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # If guards to avoid repeated traversals

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result