# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: (x.start, x.end))
        result = []
        cur = intervals[0]
        for i in range(len(intervals)):
            if cur.end < intervals[i].start:
                result.append(cur)
                cur = intervals[i]
            elif intervals[i].start <= cur.end:
                cur.end = max(intervals[i].end, cur.end)

        result.append(cur)
        return result


if __name__ == '__main__':
    s = Solution()
    l = [[1, 3], [2, 6], [8, 10], [15, 18]]
    p = []
    for v in l:
        p.append(Interval(v[0], v[1]))
    ret = s.merge(p)
    for v in ret:
        print("[{}, {}] ".format(v.start, v.end))
