# Edit Distance
# Solved
# You are given two strings word1 and word2, each consisting of lowercase English letters.
#
# You are allowed to perform three operations on word1 an unlimited number of times:
#
# Insert a character at any position
# Delete a character at any position
# Replace a character at any position
# Return the minimum number of operations to make word1 equal word2.
#
# Example 1:
#
# Input: word1 = "monkeys", word2 = "money"
#
# Output: 2
# Explanation:
# monkeys -> monkey (remove s)
# monkey -> monkey (remove k)
#
# Example 2:
#
# Input: word1 = "neatcdee", word2 = "neetcode"
#
# Output: 3
# Explanation:
# neatcdee -> neetcdee (replace a with e)
# neetcdee -> neetcde (remove last e)
# neetcde -> neetcode (insert o)
#
# Constraints:
#
# 0 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [
            [0] * (n + 1) for _ in range(m + 1)
        ]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return dp[m][n]
