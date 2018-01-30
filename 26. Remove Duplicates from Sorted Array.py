class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        while i < len(nums):
            if j == 0 or nums[j - 1] != nums[i]:
                nums[j] = nums[i]
                j = j + 1
                i = i + 1
            else:
                i = i + 1

        return j

