class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for i in range(n)] for j in range(n)]

        v = 1
        x, y = 0, 0
        while x < (n + 1) // 2 and y < (n + 1) // 2:
            b = y
            e = n - y
            for i in range(b, e):
                result[x][i] = v
                v = v + 1

            if not (x < n - x - 1):
                break

            b = x + 1
            e = n - x
            for i in range(b, e):
                result[i][n - y - 1] = v
                v = v + 1

            if not (y < n - y - 1):
                break

            b = n - y - 2
            e = y
            for i in range(b, e, -1):
                result[n - x - 1][i] = v
                v = v + 1

            b = n - x - 1
            e = x
            for i in range(b, e, -1):
                result[i][y] = v
                v = v + 1

            x = x + 1
            y = y + 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(2))
