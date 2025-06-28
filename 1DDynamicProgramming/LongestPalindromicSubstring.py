# Longest Palindromic Substring
# Solved
# Given a string s, return the longest substring of s that is a palindrome.
#
# A palindrome is a string that reads the same forward and backward.
#
# If there are multiple palindromic substrings that have the same length, return any one of them.
#
# Example 1:
#
# Input: s = "ababd"
#
# Output: "bab"
# Explanation: Both "aba" and "bab" are valid answers.
#
# Example 2:
#
# Input: s = "abbc"
#
# Output: "bb"
# Constraints:
#
# 1 <= s.length <= 1000
# s contains only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPali(string,i,j):
            while i>=0 and j<len(string) and string[i] == string[j]:
                i -= 1
                j += 1
            return string[i+1:j]

        solution = ""
        for i in range(len(s)):
            solution = max(solution,isPali(s,i,i),isPali(s,i,i+1),key=len)
        return solution