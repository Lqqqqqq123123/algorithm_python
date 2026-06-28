from typing import List
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        f = [0] * (n + 10)

        res = 0

        for i in range(1, n):
            if s[i] == '(':
                continue

            if s[i] == ')':
                if s[i - 1] == '(':
                    f[i] = f[i - 2] + 2
                else:
                    if s[i - 1] == ')':
                        pre = i - f[i - 1]
                        if s[pre] == '(':
                            f[i] = f[i - 1] + 2 + f[pre] - 1


            res = max(res, f[i])

        return res
