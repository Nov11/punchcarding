class Solution:
    table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        last = ''
        for v in s:
            if last == '':
                result = Solution.table[v]
            else:
                result = result + Solution.table[v]
                if Solution.table[last] < Solution.table[v]:
                    result = result - 2 * Solution.table[last]
            last = v

        return result