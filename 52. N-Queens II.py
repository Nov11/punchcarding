class Solution:
    def work(self, cur, n, left, mid, right):
        if cur == n:
            return 1
        result = 0
        taken = left | mid | right
        for i in range(n):
            mask = 1 << (n - i - 1)
            if (taken & mask) == 0:
                result = result + self.work(cur + 1, n, (left | mask) << 1, (mid | mask), (right | mask) >> 1)
        return result

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.work(0, n, 0, 0, 0)
