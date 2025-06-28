# Longest Common Prefix
# Solved
# You are given an array of strings strs. Return the longest common prefix of all the strings.
#
# If there is no longest common prefix, return an empty string "".
#
# Example 1:
#
# Input: strs = ["bat","bag","bank","band"]
#
# Output: "ba"
# Example 2:
#
# Input: strs = ["dance","dag","danger","damage"]
#
# Output: "da"
# Example 3:
#
# Input: strs = ["neet","feet"]
#
# Output: ""
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] is made up of lowercase English letters if it is non-empty.
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or word[i]!=char:
                    return strs[0][:i]
        return strs[0]