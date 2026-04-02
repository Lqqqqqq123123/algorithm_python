import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stack = []
res = [0] * n


for i in range(n):
    while stack and stack[-1] >= a[i]: stack.pop()
    res[i] = stack[-1] if stack else -1
    stack.append(a[i])

for i in res: print(i, end=' ')    