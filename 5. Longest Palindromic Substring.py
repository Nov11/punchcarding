class Solution:
    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l = l - 1
            r = r + 1
        return s[l + 1: r]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''

        for i in range(len(s)):
            even = self.expand(s, i, i + 1)
            odd = self.expand(s, i, i)
            if len(result) < len(even):
                result = even
            if len(result) < len(odd):
                result = odd

        return result