class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != 9 or len(board[0]) != 9:
            return False

        for i in range(0, 9):
            tmp = {}
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                x = tmp.get(board[i][j], 0)
                if x == 1:
                    return False
                tmp[board[i][j]] = x + 1

        for j in range(0, 9):
            tmp = {}
            for i in range(0, 9):
                if board[i][j] == '.':
                    continue
                x = tmp.get(board[i][j], 0)
                if x == 1:
                    return False
                tmp[board[i][j]] = x + 1

        for i in range(0, 3):
            for j in range(0, 3):
                ii = i * 3
                jj = j * 3
                tmp = {}
                for n in range(ii, ii + 3):
                    for m in range(jj, jj + 3):
                        if board[n][m] == '.':
                            continue
                        x = tmp.get(board[n][m], 0)
                        if x == 1:
                            return False
                        tmp[board[n][m]] = x + 1

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([[".","8","7","6","5","4","3","2","1"],
                           ["2",".",".",".",".",".",".",".","."],
                           ["3",".",".",".",".",".",".",".","."],
                           ["4",".",".",".",".",".",".",".","."],
                           ["5",".",".",".",".",".",".",".","."],
                           ["6",".",".",".",".",".",".",".","."],
                           ["7",".",".",".",".",".",".",".","."],
                           ["8",".",".",".",".",".",".",".","."],
                           ["9",".",".",".",".",".",".",".","."]]))