import sys
input = sys.stdin.readline
inf = 0x3f3f3f3f
def main():
    n = int(input())
    g = [[] for _ in range(n)]
    f = [[-inf] * (n + 1) for _ in range(n)]
    for i in range(n):
        g[i] = list(map(int, input().split()))
    
    f[0][0] = g[0][0]

    for i in range(1, n):
        for j, num in enumerate(g[i]):
            f[i][j] = max(f[i][j], f[i - 1][j] + num)
            if j - 1 >= 0: f[i][j] = max(f[i][j], f[i - 1][j - 1] + num)
    res = -inf        
    for j, num in enumerate (f[n - 1]):
        res = max(res, num)
    
    print(res)

main()

    