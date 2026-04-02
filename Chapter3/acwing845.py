import sys
from collections import defaultdict
from collections import deque
# 快读
r = sys.stdin.readline


def bfs(start, ed):
    
    q = deque([start])
    dist = defaultdict(int) # 存储从start到其他点的最短距离
    dist[start] = 0


    while q:
        t = q.popleft()
        # 找到x的位置
        pos = 0
        for i in range(len(t)):
            if t[i] == 'x':
                pos = i
                break 
        
        # 转成 二维坐标
        x, y = pos // 3, pos % 3

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3: # 越界
                continue
            # 看看当前状态是否已经找到过了
            temp = list(t)
            temp[pos], temp[nx * 3 + ny] = temp[nx * 3 + ny], temp[pos]
            newState = "".join(temp)

            if newState in dist:
                continue
            dist[newState] = dist[t] + 1
            if newState == ed: # 找到终点
                return dist[newState]
            q.append(newState) # 添加进队列

    


def main():
    start = "".join(r().split())
    ed = "12345678x"
    print(bfs(start, ed))
    

if __name__ == '__main__':
    main()