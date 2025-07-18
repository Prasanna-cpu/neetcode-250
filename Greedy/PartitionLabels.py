# Partition Labels
# Solved
# You are given a string s consisting of lowercase english letters.
#
# We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.
#
# Return a list of integers representing the size of these substrings in the order they appear in the string.
#
# Example 1:
#
# Input: s = "xyxxyzbzbbisl"
#
# Output: [5, 5, 1, 1, 1]
# Explanation: The string can be split into ["xyxxy", "zbzbb", "i", "s", "l"].
#
# Example 2:
#
# Input: s = "abcabc"
#
# Output: [6]
# Constraints:
#
# 1 <= s.length <= 100

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {ch: i for i, ch in enumerate(s)}
        result = []

        start = end = 0

        for i, ch in enumerate(s):
            end = max(end, last_index[ch])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result
