from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(lambda: [])
        for s in strs:
            sorted_s = ''.join(sorted(s))
            dic[sorted_s].append(s)

        # 构造答案
        res = []
        for k in dic:
            res.append(dic[k])
        return res