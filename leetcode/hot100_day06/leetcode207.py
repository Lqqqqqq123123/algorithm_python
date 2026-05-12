from collections import deque
from typing import List, Optional

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 邻接表存图
        g =[[] for _ in range(numCourses)]
        d = [0] * numCourses # 节点的入度
        res = []
        # 2. 队列
        q = deque()

        # 3. 构建图（有向图）
        for a, b in prerequisites:
            g[b].append(a)
            d[a] += 1

        # 4. topsort
        for i in range(numCourses):
            if d[i] == 0:
                q.append(i)
                res.append(i)

        while q:
            cur = q.popleft()
            for ne in g[cur]:
                d[ne] -= 1
                if d[ne] == 0:
                    q.append(ne)
                    res.append(ne)

        return len(res) == numCourses



