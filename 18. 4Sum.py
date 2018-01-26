class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        result = []
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    tmp = nums[i] + nums[j] + nums[k] + nums[l]
                    if tmp == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k = k + 1
                        while k < l and nums[k] == nums[k - 1]:
                            k = k + 1
                        l = l - 1
                        while k < l and nums[l] == nums[l + 1]:
                            l = l - 1
                    elif tmp > target:
                        l = l - 1
                    else:
                        k = k + 1
                j = j + 1
                while j < len(nums) - 2 and nums[j] == nums[j - 1]:
                    j = j + 1
            i = i + 1
            while i < len(nums) - 3 and nums[i] == nums[i - 1]:
                i = i + 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2],
                    0))
