class Solution:
    def factor(self, n):
        result = 1
        while n > 1:
            result = result * n
            n = n - 1
        return result

    def work(self, lst, kth):
        if len(lst) == 1:
            return str(lst[0])
        bucket = self.factor(len(lst) - 1)
        num = lst[(kth - 1) // bucket]
        lst.remove(num)
        return str(num) + self.work(lst, kth % bucket)

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return self.work([i for i in range(1, n + 1)], k)
