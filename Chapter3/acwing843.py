import sys
input = sys.stdin.readline
w = sys.stdout.write

n = int(input())

g = [['.' for _ in range(n)] for _ in range(n)] # 皇后棋盘

col, dj, jd = [0] * n, [0] * (2 * n - 1), [0] * (2 * n - 1)


def dfs(row : int, k:int):
    if(row == n):
        if k == n:
            for i in range(n):
                w(g[i])
            w("\n")
        return 
    
    for i in range(n):
        # 如果这里不能放，就跳过
        if col[i] or dj[i + row]  or jd[row - i + n]:
            continue
        col[i] = dj[i + row] = jd[row - i + n] = 1
        g[row][i] = 'Q'
        dfs(row + 1, k + 1)
        g[row][i] = '.'
        col[i] = dj[i + row] = jd[row - i + n] = 0
    


dfs(0, 0)


