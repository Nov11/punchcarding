class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        lst = [""] * numRows

        cur = 0
        down = True
        for v in s:
            lst[cur] = lst[cur] + v
            if down:
                if cur + 1 == numRows:
                    down = False
                    cur = numRows - 2
                else:
                    cur = cur + 1
            else:
                if numRows == 2 and cur == 0:
                    down = True
                    cur = cur + 1
                elif numRows != 2 and cur == 1:
                    down = True
                    cur = 0
                else:
                    cur = cur - 1

        return "".join(lst)


if __name__ == '__main__':
    s = Solution()
    print(s.convert("01234567890", 2))


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        tmp = [''] * numRows

        i = 0
        down = True
        for v in s:
            tmp[i] = tmp[i] + v
            if numRows == 2:
                if i == 0:
                    i = 1
                else:
                    i = 0
            else:
                if down:
                    i = i + 1
                    if i == numRows:
                        down = False
                        i = numRows - 2
                else:
                    i = i - 1
                    if i == 0:
                        down = True

        return "".join(tmp)

