class Solution1:
    def make(self, pattern):
        self.next = [0] * len(pattern)
        self.next[0] = -1
        if len(pattern) == 1:
            return
        self.next[1] = 0

        for i in range(2, len(pattern)):
            j = i - 1
            while j >= 1 and pattern[self.next[j]] != pattern[i - 1]:
                j = self.next[j]
            if j < 1:
                self.next[i] = 0
            else:
                self.next[i] = self.next[j] + 1

    def match(self, s, p):
        self.make(p)
        j = 0
        for i in range(len(s)):
            if s[i] == p[j]:
                j = j + 1
            else:
                while j >= 0 and p[j] != s[i]:
                    j = self.next[j]
                if j < 0:
                    j = 0
                else:
                    j = j + 1

            if j == len(self.next):
                return i + 1 - len(p)
        return -1

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        return self.match(haystack, needle)


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1

        next = [0] * len(needle)
        next[0] = -1
        for i in range(2, len(needle)):
            j = i - 1
            while next[j] >= 0 and needle[next[j]] != needle[i - 1]:
                j = next[j]
            if next[j] < 0:
                next[i] = 0
            else:
                next[i] = next[j] + 1

        j = 0
        for i in range(len(haystack)):
            while j >= 0 and haystack[i] != needle[j]:
                j = next[j]
            if j < 0:
                j = 0
            elif haystack[i] == needle[j]:
                j = j + 1
                if j == len(needle):
                    return i + 1 - len(needle)
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("mississippi","pi"))

