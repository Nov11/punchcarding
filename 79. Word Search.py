class Solution:

    def match(self, board, word, x, y, mark, m, n, idx):
        if idx == len(word):
            return True
        row = [1, -1, 0, 0]
        col = [0, 0, -1, 1]
        for i in range(4):
            nx = x + row[i]
            ny = y + col[i]
            if nx >= 0 and nx < m and ny >= 0 and ny < n and board[nx][ny] == word[idx] and mark[nx][ny] == 0:
                mark[nx][ny] = 1
                if self.match(board, word, nx, ny, mark, m, n, idx + 1):
                    return True
                mark[nx][ny] = 0
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        if len(word) == 0:
            return True
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0]:
                    mark = [[0 for jj in range(n)] for kk in range(m)]
                    mark[i][j] = 1
                    if self.match(board, word, i, j, mark, m, n, 1):
                        return True
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]

    s = Solution()
    print(s.exist(board, "ABCESEEEFS"))
