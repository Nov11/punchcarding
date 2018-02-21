class Solution:
    def work(self, s, n, k):
        result = []
        if k == 1:
            for i in range(s, n + 1):
                result.append([i])
            return result
        for i in range(s, n + 2 - k):
            ret = self.work(i + 1, n, k - 1)
            for v in ret:
                tmp = v[:]
                tmp.append(i)
                result.append(tmp)
        return result
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.work(1, n, k)

if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
