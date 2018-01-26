class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for v in s:
            if v == '(' or v == '[' or v == '{':
                stk.append(v)
            else:
                if len(stk) == 0:
                    if (v == ')' or v == ']' or v == '}'):
                        return False
                else:
                    if v == ']' and stk[-1] != '[':
                        return False
                    if v == '}' and stk[-1] != '{':
                        return False
                    if v == ')' and stk[-1] != '(':
                        return False
                    stk = stk[:-1]
        return len(stk) == 0

