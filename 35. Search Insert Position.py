class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        b = 0
        e = len(nums)
        while b < e:
            mid = (e + b) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid
            else:
                b = mid + 1
        return b
