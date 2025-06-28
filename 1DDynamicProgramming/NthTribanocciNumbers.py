# N-th Tribonacci Number
# Solved
# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
#
# Example 1:
#
# Input: n = 3
#
# Output: 2
# Explanation:
# T_3 = 0 + 1 + 1 = 2
#
# Example 2:
#
# Input: n = 21
#
# Output: 121415
# Constraints:
#
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n in (1, 2):
            return 1

        a, b, c = 0, 1, 1

        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
