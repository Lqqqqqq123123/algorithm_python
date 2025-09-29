# acwing798：二维差分模板题

n, m, q = map(int, input().split())

a = [[0] * (m + 10) for _ in range(n + 2)]
d = [[0] * (m + 10) for _ in range(n + 2)]

# 读入原始数组
for i in range(1, n + 1):
    a[i][1: m + 1] = list(map(int, input().split()))

# 计算差分数组
for i in range(1, n + 1):
    for j in range(1, m + 1):
        d[i][j] = a[i][j] - a[i - 1][j] - a[i][j - 1] + a[i - 1][j - 1]

# 处理操作
for i in range(q):
    x1, y1, x2, y2, c = map(int, input().split())
    d[x1][y1] += c; d[x2 + 1][y1] -= c; d[x1][y2 + 1] -=c; d[x2 + 1][y2 + 1] += c;

# 求出前缀和
for i in range(1, n + 1):
    for j in range(1, m + 1):
        a[i][j] = d[i][j] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]
        print(a[i][j], end=' ')
    print()