class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}
        result = 0
        start = 0
        for i, v in enumerate(s):
            hash[v] = hash.get(v, 0) + 1
            while hash.get(v) != 1:
                hash[s[start]] = hash[s[start]] - 1
                start = start + 1
            result = max(result, i - start + 1)

        return result

if __name__ == '__main__':
	s = Solution()
	print(s.lengthOfLongestSubstring("ggububgvfk"))
