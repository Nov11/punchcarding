class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True

        reach = 0
        i = 0
        while i < len(nums) - 1 and i <= reach:
            reach = max(reach, i + nums[i])
            i = i + 1
        return reach >= len(nums) - 1