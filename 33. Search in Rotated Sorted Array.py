class Solution:
    def find(self, nums, b, e, t):
        while b <= e:
            mid = (e + b) // 2
            if nums[mid] == t:
                return mid
            elif nums[mid] > t:
                e = mid - 1
            else:
                b = mid + 1
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        b = 0
        e = len(nums) - 1
        while b <= e:
            if nums[b] <= nums[e]:
                return self.find(nums, b, e, target)

            mid = (e + b) // 2
            if nums[mid] == target:
                return mid

            if mid == b:
                b = mid + 1
            elif nums[mid] > nums[b]:
                if target < nums[mid] and target >= nums[b]:
                    e = mid - 1
                else:
                    b = mid + 1
            else:
                if target > nums[mid] and target <= nums[e]:
                    b = mid + 1
                else:
                    e = mid - 1

        return -1