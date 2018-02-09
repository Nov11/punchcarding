class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        first, reach = 0, 0
        while reach + 1 < len(nums):
            last = reach
            for i in range(first, last + 1):
                reach = max(reach, nums[i] + i)
            first = last + 1
            step = step + 1
        return step