class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if n == 0:
            return
        for i in range(m):
            b = 0
            e = n - 1
            while b < e:
                matrix[i][b], matrix[i][e] = matrix[i][e], matrix[i][b]
                b = b + 1
                e = e - 1

        for i in range(m):
            j = 0
            while j < n - 1 - i:
                matrix[i][j], matrix[n - j - 1][m - i - 1] = matrix[n - j - 1][m - i - 1], matrix[i][j]
                j = j + 1