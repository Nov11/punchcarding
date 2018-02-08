class Solution:
    def work(self, s1, s2):
        result = ''
        while len(s1) and len(s2):
            if s1[0] == s2[0]:
                result = result + s1[0]
                s1 = s1[1:]
                s2 = s2[1:]
            else:
                break
        return result

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        if len(strs) == 1:
            return strs[0]

        result = strs[0]
        for i in range(1, len(strs)):
            result = self.work(strs[i], result)
            if result == '':
                break

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['','b']))