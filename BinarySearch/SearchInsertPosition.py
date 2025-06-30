# Search Insert Position
# Solved
# You are given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
#
# Input: nums = [-1,0,2,4,6,8], target = 5
#
# Output: 4
# Example 2:
#
# Input: nums = [-1,0,2,4,6,8], target = 10
#
# Output: 6
# Constraints:
#
# 1 <= nums.length <= 10,000.
# -10,000 < nums[i], target < 10,000
# nums contains distinct values sorted in ascending order.
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left

