class Solution:
    def setZeroes(self, matrix):
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

        colZero = False
        for v in matrix[0]:
            if v == 0:
                colZero = True
                break
        rowZero = False
        for i in range(m):
            if matrix[i][0] == 0:
                rowZero = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0 for _ in range(n)]
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if colZero:
            matrix[0] = [0 for _ in range(n)]
        if rowZero:
            for i in range(m):
                matrix[i][0] = 0

