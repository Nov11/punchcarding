class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        size = len(digits)
        carry = 1
        for i in range(size - 1, -1, -1):
            digits[i] = digits[i] + carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
            if carry == 0:
                break

        if carry:
            digits.insert(0, 1)
        return digits