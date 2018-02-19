class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tmp = path.split(sep='/')
        stk = []
        for v in tmp:
            if v == '' or v == '.':
                continue
            elif v == '..':
                if len(stk) != 0:
                    stk.pop()
            else:
                stk.append(v)

        if len(stk) == 0:
            return '/'
        result = ''
        for v in stk:
            result += '/'
            result += v
        return result