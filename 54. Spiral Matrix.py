class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        x = 0
        y = 0
        result = []
        while x < (m + 1) // 2 and y < (n + 1) // 2:
            b = y
            e = n - y
            for i in range(b, e):
                result.append(matrix[x][i])

            if not (x < m - x - 1):
                break

            b = x + 1
            e = m - x
            for i in range(b, e):
                result.append(matrix[i][n - 1 - y])

            if not (y < n - y - 1):
                break

            b = n - y - 2
            e = y
            for i in range(b, e, -1):
                result.append(matrix[m - 1 - x][i])

            b = m - 1 - x
            e = x
            for i in range(b, e, -1):
                result.append(matrix[i][y])

            x = x + 1
            y = y + 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
