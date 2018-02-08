class Solution:
    table = {'0': '', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'nmo', '7': 'prqs', '8': 'tuv',
             '9': 'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if len(digits) == 0:
            return result
        if len(digits) == 1:
            return list(self.table[digits[0]])

        ret = self.letterCombinations(digits[1:])

        for v in list(self.table[digits[0]]):
            for j in ret:
                result.append(v + j)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
