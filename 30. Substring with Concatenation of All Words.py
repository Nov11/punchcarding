class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        if len(words[0]) == 0:
            return [x for x in range(len(s) + 1)]

        result = []
        table = {}
        size = len(words[0])
        length = size * len(words)

        for v in words:
            table[v] = table.get(v, 0) + 1

        start = 0
        while start + length <= len(s):
            t1 = dict(table)
            cur = start
            while cur < start + length:
                curStr = s[cur:cur+size]
                if t1.get(curStr, -1) < 1:
                    break
                else:
                    t1[curStr] = t1[curStr] - 1
                    cur = cur + size

            if cur == start + length:
                result.append(start)
            start = start + 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("ababaab",
["ab","ba","ba"]))
