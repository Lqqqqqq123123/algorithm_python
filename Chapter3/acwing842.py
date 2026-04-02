import sys

input = sys.stdin.readline
w = sys.stdout.write

n = int(input())

st, path = [0] * (n + 1), [0] * n

def dfs(u):
    if(u == n):
        w.write(" ".join(map(str, path)) + "\n")
        return
    
    for i in range(1, n):
        if(st[i]):
            continue
        path[u] = i; st[i] = 1
        dfs(u + 1)
        st[i] = 0


dfs(0)

