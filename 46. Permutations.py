class Solution:
    def nextP(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] > nums[i + 1]:
            i = i - 1
        if i < 0:
            nums.reverse()
            return
        j = len(nums) - 1
        while j > i and nums[j] < nums[i]:
            j = j - 1
        nums[i], nums[j] = nums[j], nums[i]
        i = i + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j = j - 1

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [nums[:]]
        while True:
            self.nextP(nums)
            print(nums)
            if nums == result[0]:
                break
            result.append(nums[:])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
