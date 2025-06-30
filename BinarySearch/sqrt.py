# Sqrt(x)
# Solved
# You are given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# Example 1:
#
# Input: x = 9
#
# Output: 3
# Example 2:
#
# Input: x = 13
#
# Output: 3
# Constraints:
#
# 0 <= x <= ((2^31)-1)

class Solution:
    def mySqrt(self, x: int) -> int:

        if x in (0, 1):
            return x

        low = 0
        high = x

        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
