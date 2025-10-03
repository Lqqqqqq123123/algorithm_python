import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


i, j = 0, 0

for j in range(m):
    if a[i] == b[j]: i += 1
    

print("Yes") if i == n else print("No")
