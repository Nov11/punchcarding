class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        for i in range(1, n):
            grid[0][i] = grid[0][i] + grid[0][i - 1]

        for i in range(1, m):
            grid[i][0] = grid[i][0] + grid[i - 1][0]
            for j in range(1, n):
                grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]