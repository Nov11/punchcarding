class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        assert len(nums) >= 3
        nums.sort()

        diff = 2147483647
        result = 0
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp == target:
                    return target
                else:
                    if abs(tmp - target) < diff:
                        diff = abs(tmp - target)
                        result = tmp
                    if tmp > target:
                        k = k - 1
                    else:
                        j = j + 1

            i = i + 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([1, 2, 5, 10, 11],
                            12))
