class Solution:
    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l = l - 1
            r = r + 1
        return s[l + 1:r]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        for i in range(len(s)):
            odd = self.expand(s, i, i)
            even = self.expand(s, i, i + 1)
            if len(ret) < len(odd):
                ret = odd
            if len(ret) < len(even):
                ret = even

        return ret
