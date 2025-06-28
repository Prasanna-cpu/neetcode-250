# Contains Duplicate II
# Solved
# You are given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k, otherwise return false.
#
# Example 1:
#
# Input: nums = [1,2,3,1], k = 3
#
# Output: true
# Example 2:
#
# Input: nums = [2,1,2], k = 1
#
# Output: false
# Constraints:
#
# 1 <= nums.length <= 100,000
# -1,000,000,000 <= nums[i] <= 1,000,000,000
# 0 <= k <= 100,000

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])

            if len(seen) > k:
                seen.remove(nums[i - k])
        return False

