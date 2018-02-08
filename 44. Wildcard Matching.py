class Solution:
    def work(self, s, p):
        i = 0
        j = 0
        prevj = -1
        previ = -1
        while i < len(s):
            if j < len(p) and p[j] == '*':
                prevj = j
                previ = i
                j = j + 1
            elif j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i = i + 1
                j = j + 1
            else:
                if prevj == -1:
                    return False
                else:
                    j = prevj + 1
                    i = previ + 1
                    previ = i

        return j == len(p) or (j + 1 == len(p) and p[-1] == '*')

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        j = 0
        np = ''
        while j < len(p):
            if p[j] != '*' or not (j - 1 >= 0 and p[j - 1] == '*'):
                np = np + p[j]
                j = j + 1
            else:
                j = j + 1

        return self.work(s, np)

if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("aa", "a"))
