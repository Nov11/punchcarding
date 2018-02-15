class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n <= 0 or m <= 0:
            return 0

        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[n - 1]