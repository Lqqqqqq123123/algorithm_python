class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        s = ' ' + s
        f = [0] * (n + 10)
        res = 0
        for i in range(2, n + 1):
            if s[i] == '(':
                f[i] = 0
            else:
                # i - 1 是左括号
                if s[i - 1] == '(':
                    f[i] = 2 + f[i - 2]
                elif s[i - 1] == ')':
                    pre = i - 1 - f[i - 1]
                    if s[pre] == '(':
                        f[i] = 2 + f[i - 1] + f[pre - 1]

            res = max(res, f[i])

        return res


