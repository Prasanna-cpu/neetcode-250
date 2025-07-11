# Merge Sorted Array
# Solved
# You are given two integer arrays nums1 and nums2, both sorted in non-decreasing order, along with two integers m and n, where:
#
# m is the number of valid elements in nums1,
# n is the number of elements in nums2.
# The array nums1 has a total length of (m+n), with the first m elements containing the values to be merged, and the last n elements set to 0 as placeholders.
#
# Your task is to merge the two arrays such that the final merged array is also sorted in non-decreasing order and stored entirely within nums1.
# You must modify nums1 in-place and do not return anything from the function.
#
# Example 1:
#
# Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2
#
# Output: [1,2,10,20,20,40]
# Example 2:
#
# Input: nums1 = [0,0], m = 0, nums2 = [1,2], n = 2
#
# Output: [1,2]
# Constraints:
#
# 0 <= m, n <= 200
# 1 <= (m + n) <= 200
# nums1.length == (m + n)
# nums2.length == n
# -1,000,000,000 <= nums1[i], nums2[i] <= 1,000,000,000

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

