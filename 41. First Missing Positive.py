class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == i + 1:
                i = i + 1
                continue
            if nums[i] < 1 or nums[i] > j + 1:
                nums[i], nums[j] = nums[j], nums[i]
                j = j - 1
                continue
            if nums[nums[i] - 1] == nums[i]:
                i = i + 1
                continue
            tmp = nums[i]
            nums[i] = nums[tmp - 1]
            nums[tmp - 1] = tmp
            # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([2,1]))