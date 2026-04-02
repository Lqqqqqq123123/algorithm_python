class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, pos, n = 0, 0, len(s)

        # odd
        for i in range(n):
            l, r = i - 1, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if res < (r - 1 - l):
                res = r - l - 1
                pos = l + 1

        # even
        for i in range(n):
            l, r = i - 1, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if res < (r - 1 - l):
                res = r - l - 1
                pos = l + 1

        return s[pos:pos + res]

