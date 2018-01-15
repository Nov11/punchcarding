class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = x * -1
        ret = 0
        while x:
            ret = 10 * ret
            ret = ret + x % 10
            x = x // 10
        ret = ret * sign
        if ret > 2147483647 or ret < -2147483648:
            return 0
        return ret
    