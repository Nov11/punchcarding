class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)

        length = len1 + len2
        if length % 2 == 1:
            return self.work(nums1, 0, len1, nums2, 0, len2, length // 2 + 1)

        return self.work(nums1, 0, len1, nums2, 0, len2, length // 2) \
               + self.work(nums1, 0, len1, nums2, 0, len2, length // 2 + 1)

    def work(self, nums1, b1, e1, nums2, b2, e2, k):
        if e1 - b1 > e2 - b2:
            return self.work(nums2, b2, e2, nums1, b1, e1, k)

        if b1 == e1:
            return nums2[b2 + k - 1]

        if k == 1:
            return min(nums1[b1], nums2[b2])

        i1 = min(e1 - b1, k // 2)
        i2 = min(e2 - b2, k // 2)

        if nums1[b1 + i1 - 1] <= nums2[b2 + i2 - 1]:
            return self.work(nums1, b1 + i1, e1, nums2, b2, e2, k - i1)

        return self.work(nums1, b1, e1, nums2, b2 + i2, e2, k - i2)


if __name__ == '__main__':
    l1 = [1,3]
    l2 = [2]
    s = Solution()
    print(s.findMedianSortedArrays(l1, l2))