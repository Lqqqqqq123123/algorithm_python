from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        f = [False] * (n + 1)
        dic = set(wordDict)

        # 计算状态
        f[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if f[j] and s[j:i + 1] in dic:
                    f[i] = True
                    break

        return f[n]
