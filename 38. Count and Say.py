class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        v = '1'
        for i in range(1, n):
            s = ''
            j = 0
            while j < len(v):
                c = v[j]
                cnt = 1
                j = j + 1
                while j < len(v) and c == v[j]:
                    cnt = cnt + 1
                    j = j + 1
                s = s + str(cnt) + c
            v = s

        return v