import sys

input = sys.stdin.readline

n = int(input())

stk, res = [], [0] * n

arr = list(map(int, input().split()))


for i in range(n):
    while stk and stk[-1] >= arr[i]: stk.pop()
    if stk: res[i] = stk[-1]
    else: res[i] = -1

    stk.append(arr[i])


print(*res)