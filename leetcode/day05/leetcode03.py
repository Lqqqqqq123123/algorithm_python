from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 记录当前字串包含字符的情况
        dic = defaultdict(lambda : 0)
        n = len(s)
        res, i, j = 1, 0, 0
        while i < n:
            dic[s[i]] += 1
            while dic[s[i]] > 1:
                dic[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
            i += 1
        return res