class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        size = 0
        while x // (10 ** size):
            size = size + 1

        if size <= 1:
            return True

        for i in range(0, size // 2):
            low = x // (10 ** i) % 10

            high = x // (10 ** (size - 1 - i)) % 10
            if low != high:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(-2147483648))
