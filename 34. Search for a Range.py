class Solution:
    def find(self, nums, func):
        b = 0
        e = len(nums)
        while b < e:
            mid = (e + b) // 2
            if func(nums[mid]):
                e = mid
            else:
                b = mid + 1

        return b

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = [self.find(nums, lambda x: x >= target), self.find(nums, lambda x: x > target)]
        if ret[0] == ret[1]:
            return [-1, -1]
        return [ret[0], ret[1] - 1]