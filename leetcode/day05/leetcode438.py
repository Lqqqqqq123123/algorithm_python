from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 哈希表
        need, cur = [0] * 26, [0] * 26
        n, m = len(s), len(p)
        res = []
        if n < m:
            return res
        # 统计 p 中每个字符出现的次数
        for c in p:
            need[ord(c) - ord('a')] += 1

        # 维护一个大小为 m 的窗口
        l, r = 0, 0
        while r < n:
            cur[ord(s[r]) - ord('a')] += 1
            if r - l + 1 == m:
                if cur == need:
                    res.append(l)
                # 缩小窗口
                cur[ord(s[l]) - ord('a')] -= 1
                l += 1
            # 移动窗口
            r += 1

        return res