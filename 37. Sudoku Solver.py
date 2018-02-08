class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

    def isValid(self, board, x, y):
        for i in range(0, 9):
            if i != x and board[i][y] == board[x][y]:
                return False
        for j in range(0, 9):
            if j != y and board[x][j] == board[x][y]:
                return False
        for ii in range(x // 3 * 3, x // 3 * 3 + 3):
            for jj in range(y // 3 * 3, y // 3 * 3 + 3):
                if not (ii == x and jj == y) and board[ii][jj] == board[x][y]:
                    return False
        return True

    def work(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    continue

                for k in range(1, 10):
                    board[i][j] = str(k)
                    if not self.isValid(board, i, j):
                        continue
                    if self.work(board):
                        return True
                board[i][j] = '.'
                return False
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.work(board)