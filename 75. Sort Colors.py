class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size <= 1:
            return
        i, j, k = 0, 0, size
        while i < k:
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1
                j = j + 1
            elif nums[i] == 1:
                i = i + 1
            else:
                k = k - 1
                nums[i], nums[k] = nums[k], nums[i]
