class Solution:
    def maxSubArrayOne(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        result = nums[0]
        prev = nums[0]
        for i in range(1, len(nums)):
            prev = max(nums[i], prev + nums[i])
            result = max(result, prev)

        return result

    def work(self, b, e, nums):
        if b + 1 == e:
            return nums[b]
        if b == e:
            return -2147483648
        mid = (b + e) // 2
        result = self.work(b, mid, nums)
        result = max(result, self.work(mid + 1, e, nums))
        lmax = 0
        prev = 0
        for i in range(mid - 1, b - 1, -1):
            prev = prev + nums[i]
            lmax = max(lmax, prev)

        rmax = 0
        prev = 0
        for i in range(mid + 1, e):
            prev = prev + nums[i]
            rmax = max(rmax, prev)

        result = max(result, nums[mid] + lmax + rmax)
        # print("{0} {1} {2}".format(b, e, result))
        return result

    def maxSubArray(self, nums):
        return self.work(0, len(nums), nums)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
