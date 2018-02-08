class Solution:
    def kth(self, a1, a2, k):
        if len(a1) > len(a2):
            return self.kth(a2, a1, k)
        if len(a1) == 0:
            return a2[k - 1]

        if k == 1:
            return min(a1[0], a2[0])

        cnt = min(k // 2, len(a1))

        if a1[cnt - 1] < a2[cnt - 1]:
            return self.kth(a1[cnt:], a2, k - cnt)
        else:
            return self.kth(a1, a2[cnt:], k - cnt)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size = len(nums1) + len(nums2)

        if size % 2:
            return self.kth(nums1, nums2, (size + 1) // 2)
        else:
            return (self.kth(nums1, nums2, size // 2) + self.kth(nums1, nums2, size // 2 + 1)) / 2


if __name__ == '__main__':
    l1 = [1, 3]
    l2 = [2]
    s = Solution()
    print(s.findMedianSortedArrays(l1, l2))
