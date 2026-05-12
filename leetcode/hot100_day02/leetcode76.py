from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if n < m:
            return ""
        minl, pos = float('inf'), 0
        need, cur = defaultdict(int), defaultdict(int)
        for c in t:
            need[c] += 1
        l, r, cnt = 0, 0, 0
        while r < n:
            cur[s[r]] += 1
            # 当前收集的字符有用
            if cur[s[r]] <= need[s[r]]:
                cnt += 1
            # 如果当前窗口已经满足答案了，找最优解
            while cnt >= m:
                if r - l + 1 < minl:
                    minl = r - l + 1
                    pos = l
                if need[s[l]] > 0:
                    cur[s[l]] -= 1
                    if cur[s[l]] < need[s[l]]:
                        cnt -= 1
                l += 1
            r += 1
            # print(l, r, cnt, sep=' ')

        return s[pos:pos + minl] if minl != float('inf') else ''
