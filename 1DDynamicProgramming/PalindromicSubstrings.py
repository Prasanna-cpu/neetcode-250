# Palindromic Substrings
# Solved
# Given a string s, return the number of substrings within s that are palindromes.
#
# A palindrome is a string that reads the same forward and backward.
#
# Example 1:
#
# Input: s = "abc"
#
# Output: 3
# Explanation: "a", "b", "c".
#
# Example 2:
#
# Input: s = "aaa"
#
# Output: 6
# Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.

class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left, right):
            res = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            return res

        count = 0
        for i in range(len(s)):
            count += expand(i, i)
            count += expand(i, i + 1)
        return count
