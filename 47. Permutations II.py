class Solution:
    def work(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i = i - 1
        if i < 0:
            nums.reverse()
            return nums

        j = len(nums) - 1
        while nums[i] >= nums[j]:
            j = j - 1

        nums[i], nums[j] = nums[j], nums[i]
        j = len(nums) - 1
        i = i + 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        while True:
            result.append(nums[:])
            self.work(nums)
            if result[0] == nums:
                break
        return result