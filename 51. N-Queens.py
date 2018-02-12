class Solution:
    def toStr(self, pattern, n):
        result = ''
        for i in range(n):
            mask = 1 << (n - i - 1)
            if pattern & mask:
                result = result + 'Q'
            else:
                result = result + '.'
        return result

    def work(self, cur, n, left, mid, right, path, result):
        if cur == n:
            result.append(path[:])
            return

        taken = left | mid | right
        for i in range(n):
            mask = 1 << (n - i - 1)
            if (taken & mask) == 0:
                path.append(self.toStr(mask, n))
                self.work(cur + 1, n, (left | mask) << 1, (mid | mask), (right | mask) >> 1, path, result)
                path.pop()

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        path = []
        self.work(0, n, 0, 0, 0, path, result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
