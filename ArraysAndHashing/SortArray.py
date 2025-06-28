# Sort an Array
# Solved
# You are given an array of integers nums, sort the array in ascending order and return it.
#
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
#
# Example 1:
#
# Input: nums = [10,9,1,1,1,2,3,1]
#
# Output: [1,1,1,1,2,3,9,10]
# Example 2:
#
# Input: nums = [5,10,2,1,3]
#
# Output: [1,2,3,5,10]
# Constraints:
#
# 1 <= nums.length <= 50,000.
# -50,000 <= nums[i] <= 50,000
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            sorted_arr = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1

            while i < len(left):
                sorted_arr.append(left[i])
                i += 1
            while j < len(right):
                sorted_arr.append(right[j])
                j += 1
            return sorted_arr

        return merge_sort(nums)
