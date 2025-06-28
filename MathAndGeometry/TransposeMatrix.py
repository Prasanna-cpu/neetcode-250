# Transpose Matrix
# Solved
# You are given a 2D integer array matrix, return the transpose of matrix.
#
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
#
# Example 1:
#
# Input: matrix = [
#     [2,1],
#     [-1,3]
# ]
#
# Output: [
#     [2,-1],
#     [1,3]
# ]
# Example 2:
#
# Input: [
#     [1,0,5],
#     [2,4,3]
# ]
#
# Output: [
#     [1,2],
#     [0,4],
#     [5,3]
# ]
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 100,000
# -1,000,000,000 <= matrix[i][j] <= 1,000,000,000

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        result = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]
        return result