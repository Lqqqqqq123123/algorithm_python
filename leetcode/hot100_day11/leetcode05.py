
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, pos = 0, 0
        n = len(s)

        # 奇数回文串
        for i in range(n):
            l, r = i - 1, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if r - 1 - l > res:
                res = r - 1 - l
                pos = l + 1

        # 偶数回文串
        for i in range(n):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if r - 1 - l > res:
                res = r - 1 - l
                pos = l + 1

        return s[pos:pos + res]