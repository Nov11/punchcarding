class Solution:
    def longestValidParenthesesSTK(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = [-1]
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                if len(stk) == 1:
                    stk[0] = i
                    continue
                stk.pop()
                result = max(result, i - stk[-1])
        return result

    def longestValidParentheses(self, s):
        dp = [0] * (len(s) + 1)
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                continue
            if i - 1 >= 0:
                if s[i - 1] == '(':
                    dp[i + 1] = dp[i - 1] + 2
                elif s[i - 1] == ')' and dp[i] != 0 and i + 1 - (2 + dp[i]) >= 0 and s[i + 1 - (2 + dp[i])] == '(':
                    dp[i + 1] = 2 + dp[i] + dp[i + 1 - (2 + dp[i])]
            result = max(result, dp[i + 1])

        return result

if __name__=='__main__':
    s = Solution()
    print(s.longestValidParentheses("(()))())("))