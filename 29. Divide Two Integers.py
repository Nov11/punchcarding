class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0
        sign = 1
        if dividend < 0:
            sign = -1
            dividend = -dividend
        if divisor < 0:
            sign = sign * -1
            divisor = -divisor

        i = 0
        while dividend >= divisor << i:
            i = i + 1
        i = i - 1

        while i >= 0:
            if dividend >= divisor << i:
                result = result + (1 << i)
                dividend = dividend - (divisor << i)
            i = i - 1

        if sign == -1:
            result = -result
        if result > 2147483647 or result < -2147483648:
            return 2147483647
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.divide(5,2))