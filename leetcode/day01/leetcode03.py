from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        cnt = defaultdict(lambda : 0)

        l, r, res = 0, 0, 0
        while r < n:
            cnt[s[r]] += 1
            while cnt[s[r]] > 1:
                cnt[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

