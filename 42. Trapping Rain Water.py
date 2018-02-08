class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = [0]
        for i in range(1, len(height)):
            left = left + [max(height[i - 1], left[-1])]
        right = [0]
        for i in range(len(height) - 2, -1, -1):
            right = [max(height[i + 1], right[0])] + right
        result = 0
        for i in range(len(height)):
            v = min(left[i], right[i]) - height[i]
            if v > 0:
                result = result + v
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.trap([4,2,3]))