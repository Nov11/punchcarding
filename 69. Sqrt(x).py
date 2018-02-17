import math


class Solution:
    def next(self, x0, x):
        return x0 - (x0 * x0 - x) / 2 / x0

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 1
        tmp = self.next(ret, x)
        for _ in range(100):
            ret = tmp
            tmp = self.next(ret, x)
        return int(ret)


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(2147395599))
