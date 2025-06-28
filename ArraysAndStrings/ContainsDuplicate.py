from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookback = set()

        for num in nums:
            if num in lookback:
                return True
            lookback.add(num)
        return False