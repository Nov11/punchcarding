class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        ret = 0
        start = 0
        cnt = 0
        for c in s :
            while dict.get(c, 0) != 0 :
                dict[s[start]] = dict[s[start]] - 1
                start = start + 1
                cnt = cnt - 1

            dict[c] = 1
            cnt = cnt + 1

            if ret < cnt:
                ret = cnt
        
        return ret

if __name__ == '__main__':
	s = Solution()
	print(s.lengthOfLongestSubstring("ggububgvfk"))
