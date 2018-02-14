# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        while i < len(intervals):
            cur = intervals[i]
            if cur.start > newInterval.end:
                intervals.insert(i, newInterval)
                return intervals
            elif cur.end < newInterval.start:
                i = i + 1
            else:
                newInterval.start = min(newInterval.start, cur.start)
                newInterval.end = max(newInterval.end, cur.end)
                del intervals[i]
        intervals.insert(len(intervals), newInterval)
        return intervals


if __name__ == '__main__':
    s = Solution()
    l1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]

    param = []
    for v in l1:
        param.append(Interval(v[0], v[1]))
    ret = s.insert(param, Interval(4, 9))
    for v in ret:
        print("[{} {}]".format(v.start, v.end))
