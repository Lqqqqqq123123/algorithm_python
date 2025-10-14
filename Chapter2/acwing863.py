import sys

input = sys.stdin.readline
prt = sys.stdout.write
sys.setrecursionlimit(1000000)

N = int(1e5 + 10)
# 并查集 初始化时：自己指向自己
p = [i for i in range(N)]


def find(x:int) -> int:
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def merge(a:int, b:int):
    A, B = find(a), find(b)
    if A != B:
        p[A] = B
    

n, m = map(int, input().split())

for i in range(m):
    op, a, b = input().split()
    if op == "M":
        merge(int(a), int(b))
    elif op == "Q":
        A, B = find(int(a)), find(int(b))
        if A == B:
            prt("Yes\n")
        else:
            prt("No\n")
