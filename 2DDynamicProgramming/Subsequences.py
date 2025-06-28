# Distinct Subsequences
# Solved
# You are given two strings s and t, both consisting of english letters.
#
# Return the number of distinct subsequences of s which are equal to t.
#
# Example 1:
#
# Input: s = "caaat", t = "cat"
#
# Output: 3
# Explanation: There are 3 ways you can generate "cat" from s.
#
# (c)aa(at)
# (c)a(a)a(t)
# (ca)aa(t)
# Example 2:
#
# Input: s = "xxyxy", t = "xy"
#
# Output: 5
# Explanation: There are 5 ways you can generate "xy" from s.
#
# (x)x(y)xy
# (x)xyx(y)
# x(x)(y)xy
# x(x)yx(y)
# xxy(x)(y)
# Constraints:
#
# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]