class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        if n == 2:
            return 2
        a1 = 1
        a2 = 2
        for i in range(3, n + 1):
            a1, a2 = a2, a1 + a2
        return a2