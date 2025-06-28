# Longest Substring Without Repeating Characters
# Solved
# Given a string s, find the length of the longest substring without duplicate characters.
#
# A substring is a contiguous sequence of characters within a string.
#
# Example 1:
#
# Input: s = "zxyzxyz"
#
# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.
#
# Example 2:
#
# Input: s = "xxxx"
#
# Output: 1
# Constraints:
#
# 0 <= s.length <= 1000
# s may consist of printable ASCII characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_index = {}
        max_len = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            char_index[s[end]] = end

            max_len = max(max_len , end-start+1)
        return max_len