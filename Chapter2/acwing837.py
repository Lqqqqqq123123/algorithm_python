import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
prt = sys.stdout.write

N = int(1e5 + 10)

p, cnt = [i for i in range(N)], [1] * N

def find(x:int) -> int:
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def merge(a:int, b:int):
    A, B = find(a), find(b)
    if A != B:
        cnt[B] += cnt[A]
        p[A] = B
    

n, m = map(int, input().split())

for i in range(m):
    lines = input().split()

    if lines[0] == "C":
        a, b = map(int, lines[1:])
        merge(a, b)
    elif lines[0] == "Q1":
        a, b = map(int, lines[1:])
        A, B = find(a), find(b)
        if A == B:
            prt("Yes\n")
        else:
            prt("No\n")
    else:
        a = int(lines[1])
        prt(str(cnt[find(a)]) + "\n")
