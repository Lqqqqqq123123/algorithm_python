import sys
from collections import deque
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    g, d, res = [[]for _ in range(n)], [0] * (n + 10), []

    for i in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        d[b] += 1

    def topsort():
        q = deque()
        for i in range(1, n + 1):
            if d[i] == 0:
                q.append(i)
                res.append(i)

        while q:
            u = q.popleft()
            for v in g[u]:
                d[v] -= 1
                if d[v] == 0:
                    q.append(v)
                    res.append(v)
        
        return len(res) == n



    if topsort():
        print(*res)
    else:
        print(-1)


    
if __name__ == '__main__':
    main()