class Solution:
    def exists(self, t, arr, b, e):
        while b < e:
            mid = b + (e - b) // 2
            if arr[mid] == t:
                return True
            elif arr[mid] > t:
                e = mid
            else :
                b = mid + 1
        return False

    def threeSumOld(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        size = len(nums)
        i = 0
        while i + 2 < size:
            v1 = nums[i]
            i2 = i + 1

            while i2 < size :
                v2 = nums[i2]
                t = (v1 + v2) * -1
                if self.exists(t, nums, i2 + 1, size):
                    result.append([v1, v2, t])
                while i2 < size and nums[i2] == v2:
                    i2 = i2 + 1

            while i < size and nums[i] == v1:
                i = i + 1
        return result

    def threeSum(self, nums):
        nums.sort()
        result = []
        i = 0
        while i + 2 < len(nums):
            t = -1 * nums[i]
            first = i + 1
            last = len(nums) - 1
            while first < last:
                tmp = nums[first] + nums[last]
                if tmp < t:
                    first = first + 1
                elif tmp > t:
                    last = last - 1
                else:
                    result.append([nums[i], nums[first], nums[last]])
                    vfirst = nums[first]
                    while first < last and vfirst == nums[first]:
                        first = first + 1
                    vlast = nums[last]
                    while first < last and vlast == nums[last]:
                        last = last - 1
            vi = nums[i]
            while i + 2 < len(nums) and vi == nums[i]:
                i = i + 1
        return result



if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))