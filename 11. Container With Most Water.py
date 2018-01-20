class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        assert(len(height) >= 2)
        l = 0
        r = len(height) - 1
        
        result = 0
        while(l < r):
            result = max(result, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        
        return result
