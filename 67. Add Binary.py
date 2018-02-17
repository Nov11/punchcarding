class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = ""
        while i >= 0 or j >= 0 or carry:
            va = 0
            if i >= 0:
                va = ord(a[i]) - ord('0')
                i = i - 1
            vb = 0
            if j >= 0:
                vb = ord(b[j]) - ord('0')
                j = j - 1

            result += (str((va + vb + carry) % 2))
            carry = (va + vb + carry) // 2

        return result[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('11', '1'))
