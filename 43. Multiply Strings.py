class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        v1 = [ord(x) - ord('0') for x in num1]
        v2 = [ord(x) - ord('0') for x in num2]
        tmp = [0] * (len(num1) + len(num2))

        for i in range(len(v1)):
            for j in range(len(v2)):
                v = v1[i] * v2[j]
                idx = i + j + 1
                tmp[idx] = v + tmp[idx]
        for i in range(len(tmp) - 1, 0, -1):
            tmp[i - 1] = tmp[i - 1] + tmp[i] // 10
            tmp[i] = tmp[i] % 10
        while len(tmp) > 1 and tmp[0] == 0:
            tmp = tmp[1:]

        return ''.join(str(x) for x in tmp)


if __name__ == "__main__":
    s = Solution()
    print(s.multiply("9", "99"))
