class Solution:
    def work(self, c, t):
        if len(c) == 0:
            return []

        if c[0] > t:
            return []

        result = []
        for i in range(len(c)):
            if c[i] == t:
                result.append([t])
                break
            else:
                ret = self.work(c[i:], t - c[i])
                for v in ret:
                    v.append(c[i])
                    result.append(v)
        return result

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.work(candidates, target)

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))