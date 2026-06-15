from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        # 记录每个字母最后出现的次数
        last = {}
        for i in range(n - 1, -1, -1):
            if s[i] not in last:
                last[s[i]] = i

        # l, r记录当前区间
        res, l, r = [], 0, 0
        cur = 0
        while r < n:
            cur = max(cur, last[s[r]])
            while r <= cur:
                cur = max(cur, last[s[r]])
                r += 1

            res.append(cur - l + 1)
            l = cur + 1


        return res


