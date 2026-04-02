import sys
input = sys.stdin.readline

def kruskual():
    n, m = map(int, input().split())
    edges, p = [], [i for i in range(n + 10)]
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append([w, u, v])

    edges.sort(lambda x : x[2])

    ans, cnt = 0, 0
    for u, v, w in edges:
        pa, pb = find(u), find(v)
        if pa != pb:
            ans += 1; cnt += 1
            p[pa] = pb
        
    
    print(ans if cnt == n - 1 else "impossible")


if __name__ == "__main__":
    kruskual()
