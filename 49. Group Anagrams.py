class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = {}
        for v in strs:
            tmp = ''.join(sorted(v))
            if table.get(tmp, 0)  == 0:
                table[tmp] = []
            table[tmp].append(v)
        result = []
        for v in table.values():
            result .append(v)
        return result