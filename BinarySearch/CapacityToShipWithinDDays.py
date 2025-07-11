# Capacity to Ship Packages Within D Days
# Solved
# A conveyor belt has packages that must be shipped from one port to another within days days.
#
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). It is not allowed to load weight more than the maximum weight capacity of the ship.
#
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
#
# Example 1:
#
# Input: weights = [2,4,6,1,3,10], days = 4
#
# Output: 10
# Explanation:
# 1st day: [2]
# 2nd day: [4,6]
# 3rd day: [1,3]
# 4th day: [10]
#
# Example 2:
#
# Input: weights = [1,2,3,4,5], days = 5
#
# Output: 5
# Explanation:
# 1st day: [1]
# 2nd day: [2]
# 3rd day: [3]
# 4th day: [4]
# 5th day: [5]
#
# Example 3:
#
# Input: weights = [1,5,4,4,2,3], days = 3
#
# Output: 8
# Explanation:
# 1st day = [1,5]
# 2nd day = [4,4]
# 3rd day = [2,3]
#
# Constraints:
#
# 1 <= days, weights.length <= 50,000
# 1 <= weights[i] <= 500


from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def isFeasible(capacity):
            days_taken = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    days_taken += 1
                    current_load = 0
                current_load += w

            return days_taken <= days

        left = max(weights)
        right = sum(weights)
        answer = right

        while left <= right:
            mid = left + (right - left) // 2
            if isFeasible(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer

