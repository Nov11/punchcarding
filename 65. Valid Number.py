class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        idx = 0
        size = len(s)
        while idx < size and s[idx] == ' ':
            idx = idx + 1
        if idx == size:
            return False

        if s[idx] == '+' or s[idx] == '-':
            idx = idx + 1
        if idx == size:
            return False

        ii = idx
        while ii < size and s[ii].isdigit():
            ii = ii + 1

        integer = ii - idx
        # if ii > idx + 1 and s[idx] == '0' and s[idx + 1] == '0':
        #     return False
        if ii == size:
            return integer > 0

        decimal = 0
        idx = ii
        if s[ii] == '.':
            idx = idx + 1
            dd = idx
            while dd < size and s[dd].isdigit():
                dd = dd + 1
            decimal = dd - idx
            if dd == size:
                return decimal > 0 or integer > 0
            if decimal == 0 and integer == 0:
                return False
            idx = dd

        if s[idx] == 'e' or s[idx] == 'E':
            idx = idx + 1
            ee = idx
            if ee == size:
                return False
            if s[ee] == '-' or s[ee] == '+':
                ee = idx + 1
                idx = idx + 1
            while ee < size and s[ee].isdigit():
                ee = ee + 1
            ex = ee - idx
            if integer == 0 and decimal == 0:
                return False
            if ex == 0:
                return False
            # if ex >= 2 and s[dd] == '0' and s[dd + 1] == '0':
            #     return False
            idx = ee

        while idx < size and s[idx] == ' ':
            idx = idx + 1
        return idx == size
