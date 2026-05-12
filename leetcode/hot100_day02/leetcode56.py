from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return  intervals
        # 1. 对区间排序
        intervals.sort(key=lambda x : x[0])

        # 2. 收集答案
        st, ed = intervals[0][0], intervals[0][1]
        ans = list()
        for i in range(1, n):
            if intervals[i][0] <= ed:
                ed = max(ed, intervals[i][1])
            else:
                ans.append([st, ed])
                st, ed = intervals[i][0], intervals[i][1]

        ans.append([st, ed])

        return ans