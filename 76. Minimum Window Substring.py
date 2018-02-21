class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        table = {}
        for i in range(len(t)):
            if table.get(t[i], -1) == -1:
                table[t[i]] = 0
            table[t[i]] = table[t[i]] + 1

        result = ''
        length = float('inf')
        q = []
        cnt = len(t)
        for i in range(len(s)):
            c = s[i]
            if table.get(c, None) is None:
                continue
            q.append((c, i))
            table[c] = table[c] - 1
            if table[c] >= 0:
                cnt = cnt - 1

            while cnt == 0:
                front = q.pop(0)
                curLength = i + 1 - front[1]
                if curLength < length:
                    length = curLength
                    result = s[front[1]: i + 1]
                table[front[0]] = table[front[0]] + 1
                if table[front[0]] > 0:
                    cnt = cnt + 1
        return result


if __name__ == '__main__':
    S = "AAABC"
    T = "ABC"
    s = Solution()
    print(s.minWindow(S, T))
