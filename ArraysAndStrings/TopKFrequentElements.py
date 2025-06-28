# Top K Frequent Elements
# Solved
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
#
# The test cases are generated such that the answer is always unique.
#
# You may return the output in any order.
#
# Example 1:
#
# Input: nums = [1,2,2,3,3,3], k = 2
#
# Output: [2,3]
# Example 2:
#
# Input: nums = [7,7], k = 1
#
# Output: [7]
# Constraints:
#
# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        freq_list = list(freq_map.items())
        freq_list.sort(key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(freq_list[i][0])
        return result
