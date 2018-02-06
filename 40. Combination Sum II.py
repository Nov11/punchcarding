class Solution:
    def work(self, c, t):
        if len(c) == 0:
            return []
        if c[0] > t:
            return []
        result = []
        for i in range(len(c)):
            if i > 0 and c[i] == c[i - 1]:
                continue
            if c[i] == t:
                result.append([c[i]])
                break
            else:
                ret = self.work(c[i + 1:], t - c[i])
                for v in ret:
                    v.append(c[i])
                    result.append(v)
        return result

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.work(candidates, target)

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))