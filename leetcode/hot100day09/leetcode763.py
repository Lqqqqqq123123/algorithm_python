from typing import List, Optional


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res, n = [], len(s)
        # 创建一个哈希表，记录每个单词最后出现的位置
        last = {}
        for i in range(n - 1, -1, -1):
            if s[i] not in last:
                last[s[i]] = i

        # 贪心的去分割字符串
        u = 0
        pre = 0
        while u < n:
            cur = last[s[u]]
            while u <= cur:
                cur = max(cur, last[s[u]])
                u += 1

            res.append(cur - pre + 1)
            pre = cur + 1

        return res
