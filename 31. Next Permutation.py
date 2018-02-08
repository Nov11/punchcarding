class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
             i = i - 1

        if i < 0:
            nums.reverse()
            return

        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j = j - 1

        nums[i], nums[j] = nums[j], nums[i]
        i = i + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j = j - 1

if __name__ == '__main__':
    s = Solution()
    n = [1, 2, 3]
    for i in range(7):
        s.nextPermutation(n)
        print(n)