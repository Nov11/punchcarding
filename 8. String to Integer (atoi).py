class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        size = len(str)
        while i < size and (str[i] == ' ' or str[i] == '\t' or str[i] == '\n' or str[i] == '\r') :
            i = i + 1
        
        if i == size :
            return 0
        
        sign = 1
        if str[i] == '-':
            sign = -1
            i = i + 1
        elif str[i] == '+':
            i = i + 1
            
        value = 0
        while i < size and str[i].isdigit():
            value = value * 10
            value = value + ord(str[i]) - ord('0')
            i = i + 1
        
        value = sign * value
        
        if value > 2147483647:
            return 2147483647
        if value < -2147483648:
            return -2147483648
        return value
