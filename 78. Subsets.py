class Solution:
    def work(self, nums, path, i, result):
        if i == len(nums):
            result.append(path[:])
            return

        path.append(nums[i])
        self.work(nums, path, i + 1, result)
        path.pop()

        self.work(nums, path, i + 1, result)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        path = []
        self.work(nums, path, 0, result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
