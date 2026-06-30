from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 思路：滑动窗口，当 r 固定后，找到满足条件的最大的l，此时满足条件的字串数量为 l + 1
        cnt = defaultdict(int)
        l, r, n = 0, 0, len(s)
        res = 0
        while r < n:
            cnt[s[r]] += 1
            # 移动 l
            while l < r and cnt[s[l]] > 1:
                cnt[s[l]] -= 1
                l += 1

            # 判断是否合法
            if cnt['a'] > 0 and cnt['b'] > 0 and cnt['c'] > 0:
                res += l + 1

            r += 1


        return res


