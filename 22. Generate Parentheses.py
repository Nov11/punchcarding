class Solution:
    def work(self, l, r):
        if l == 0 and r == 0:
            return []
        if l == 1 and r == 0:
            return ['(']
        if l == 0 and r == 1:
            return [')']
        result = []
        if l > 0:
            ret = self.work(l - 1, r)
            for v in ret:
                result.append('(' + v)
        if l < r:
            ret = self.work(l, r - 1)
            for v in ret:
                result.append(')' + v)
        return result

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.work(n, n)

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))