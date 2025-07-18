# Rotate Array
# Solved
# You are given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7,8], k = 4
#
# Output: [5,6,7,8,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [8,1,2,3,4,5,6,7]
# rotate 2 steps to the right: [7,8,1,2,3,4,5,6]
# rotate 3 steps to the right: [6,7,8,1,2,3,4,5]
# rotate 4 steps to the right: [5,6,7,8,1,2,3,4]
#
# Example 2:
#
# Input: nums = [1000,2,4,-3], k = 2
#
# Output: [4,-3,1000,2]
# Explanation:
# rotate 1 steps to the right: [-3,1000,2,4]
# rotate 2 steps to the right: [4,-3,1000,2]
#
# Constraints:
#
# 1 <= nums.length <= 100,000
# -(2^31) <= nums[i] <= ((2^31)-1)
# 0 <= k <= 100,000
# Follow up: Could you do it in-place with O(1) extra space?
#


from typing import List

class Solution:
    def reverse(self, start, end, nums):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        self.reverse(0, n - 1, nums)
        self.reverse(0, k - 1, nums)
        self.reverse(k, n - 1, nums)

