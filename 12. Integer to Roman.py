class Solution:
    table = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    def generate(self, digit, one, five, ten):
        if digit < 4:
            return one * digit
        if digit == 4:
            return one + five
        if digit < 9:
            return five + one * (digit - 5)
        if digit == 9:
            return one + ten

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''

        if num // 1000:
            result = result + self.generate(num // 1000, Solution.table[1000], '','')
        if num // 100 % 10:
            result = result + self.generate(num // 100 % 10, Solution.table[100], Solution.table[500], Solution.table[1000])
        if num // 10 % 10:
            result = result + self.generate(num // 10 % 10, Solution.table[10], Solution.table[50], Solution.table[100])
        if num % 10:
            result = result + self.generate(num % 10, Solution.table[1], Solution.table[5], Solution.table[10])
        return result

