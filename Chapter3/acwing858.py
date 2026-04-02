import sys
input = sys.stdin.readline
inf = 0x3f3f3f3f
def prim():
    
    n, m = map(int, input().split())
    dist, st = [inf] * (n + 10), [False] * (n + 10),
    g = [[inf for _ in range(n + 10)] for _ in range(n + 10)]
    
    for i in range(n):
        g[i][i] = 0

    for i in range(m):
        a, b, c = map(int, input().split())
        g[a][b] = min(g[a][b], c)
        g[b][a] = min(g[b][a], c)

    res = 0
    for i in range(n):
        t = -1
        for j in range(1, n + 1):
            if not st[j] and (t == -1 or dist[t] > dist[j]):t = j
        
        if i and dist[t] == inf: return inf
        if i:res += dist[t]
        st[t] = True
        for j in range(1, n + 1):
            dist[j] = min(dist[j], g[j][t])

    return res


if __name__ == '__main__':
    ans = prim()
    print(ans if ans != inf else "impossible")