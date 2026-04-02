from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s0 = strs[0]
        for i, c in enumerate(s0):
            for s in strs:
                if i >= len(s) or c != s[i]:
                    return s0[:i]

        return s0