import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

def lowbit(x : int) -> int:
    return x & -x

res = [0] * n

for i in range(n):
    while(a[i] != 0):
        a[i] -= lowbit(a[i])
        res[i] += 1
        

for i in range(n):
    print(res[i], end=' ') 