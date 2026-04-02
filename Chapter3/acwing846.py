import sys
import math
r = sys.stdin.readline
res = 0
def main():
    n = int(r.input())
    g = [[] for i in range(n)] # 邻接表

    for i in range(n - 1):
        a, b = map(int, r.input().split())
        g[a].append(b); g[b].append(a)


    dfs(0, -1, g, n)
    print(res)



def dfs(u, p, g, n):
    Max, sum = 0, 1
    # 遍历节点u的儿子
    for v in g[u]:
        if(v == p):
            continue
        s = dfs(v, u, g, n)
        Max = max(Max, s)
        sum += s
    
    Max = max(Max, n - sum)
    res = max(res, Max)
    
    return sum



if __name__ == '__main__':
    main()