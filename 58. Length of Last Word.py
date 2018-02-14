class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0[0]
        result = 0
        word = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' or s[i] == '\t' or s[i] == '\n' or s[i] == '\r':
                if not word:
                    continue
                else:
                    break
            word = True
            result = result + 1
        return result
