class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for idx, v in enumerate(nums):
            if target - v in dict :
                return (idx, dict[target - v])
            dict[v] = idx
        return ()
