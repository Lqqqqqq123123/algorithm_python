import sys

input = sys.stdin.readline


n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, 0

while j < m:
    if i < n and a[i] == b[j]: i += 1
    if i == n: break
    j += 1

print("Yes") if i == n else print("No")

