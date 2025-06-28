# Maximum Product Subarray
# Solved
# Given an integer array nums, find a subarray that has the largest product within the array and return it.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
# You can assume the output will fit into a 32-bit integer.
#
# Example 1:
#
# Input: nums = [1,2,-3,4]
#
# Output: 4
# Example 2:
#
# Input: nums = [-2,-1]
#
# Output: 2
# Constraints:
#
# 1 <= nums.length <= 1000
# -10 <= nums[i] <= 10
#
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_so_far, min_so_far = min_so_far, max_so_far

            max_so_far = max(nums[i], nums[i] * max_so_far)
            min_so_far = min(nums[i], nums[i] * min_so_far)

            result = max(result, max_so_far)

        return result
