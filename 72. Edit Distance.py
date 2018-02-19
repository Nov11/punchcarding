class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            dp[i][0] = i
        for j in range(1, len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                mod = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    mod = mod + 1
                d = dp[i - 1][j] + 1
                add = dp[i][j - 1] + 1
                dp[i][j] = min(mod, min(add, d))
        return dp[len(word1)][len(word2)]
