class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # print("s:{} p:{}\n".format(s,p))
        if len(p) == 0:
            return len(s) == 0

        if len(p) == 1:
            if len(s) != 1:
                return False
            return s[0] == p[0] or p[0] == '.'

        if p[1] != '*':
            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False

        # ---------------this will fail the last test case. TLE. I don't know why.
        # if self.isMatch(s, p[2:]):
        #     return True
        #
        # for i in range(len(s)):
        #     if s[i] == p[0] or p[0] == '.':
        #         if self.isMatch(s[i + 1:], p[2:]):
        #             return True
        #     else:
        #         break
        #
        # return False
        # ------------------ these two are identical on probing sequence.
        # ------------------ what makes the former one slower than the second one?
        # while len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
        #     if self.isMatch(s, p[2:]):
        #         return True
        #     s = s[1:]
        #
        # return self.isMatch(s, p[2:])
#         i guess string ops slows former procedure down
#         but running time is identical on my pc. em...

        # while True:
        #     if self.isMatch(s, p[2:]):
        #         return True
        #     if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
        #         s = s[1:]
        #     else:
        #         return False

        i = 0
        while True:
            if self.isMatch(s[i:], p[2:]):
                return True
            if len(s) > i and (s[i] == p[0] or p[0] == '.'):
                pass
            else:
                return False
            i = i + 1


if __name__ == '__main__':
    s = Solution()

    # assert (s.isMatch("aa", "a") == False);
    # assert (s.isMatch("aa", "aa") == True);
    # assert (s.isMatch("aa", ".*") == True);
    # assert (s.isMatch("aa", "a*") == True)
    # assert (s.isMatch("aaa", "aa") == False)
    # assert (s.isMatch("ab", ".*") == True)
    # assert (s.isMatch("aab", "c*a*b") == True)
    # assert (s.isMatch("a", ".*..a*") == False)
    # assert (s.isMatch("bbbba", ".*a*a") == True)

# assert (s.isMatch("bbbacbcbcbbbbabbbab", "b*c*c*.*.*.*ab*c") == False)
    print(s.isMatch("baccbbcbcacacbbc","c*.*b*c*ba*b*b*.a*"))


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0

        if len(p) == 1:
            return len(s) == 1 and (s[0] == p[0] or p[0] == '.')

        if p[1] != '*':
            return len(s) != 0 and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])

        while True:
            if self.isMatch(s, p[2:]):
                return True

            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                s = s[1:]
            else:
                break
        return False