
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 两种思路
        # 1. 直接枚举所以技术回文和偶数回文串，找出最优解即可
        n, max_len, res = len(s), 1, ''

        # 枚举奇数回文串
        for i in range(n):
            l, r = i - 1, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l + 1 > max_len:
                max_len = r - l + 1
                res = s[l + 1:r]

        # 枚举偶数回文串
        for i in range(n):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l + 1 > max_len:
                max_len = r - l + 1
                res = s[l + 1:r]


        return res  

