class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j = j + 1
            i = i + 1
        return j