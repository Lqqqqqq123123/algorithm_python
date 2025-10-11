import sys
input = sys.stdin.readline


stk = list()

m = int(input())

for i in range(m):
    lines = input().split()
    op = lines[0]
    if op == 'push':
        # push 操作
        stk.append(int(lines[1]))
    elif op == 'pop':
        # pop 操作
        stk.pop()
    elif op == 'empty':
        # empty 操作
        print("YES" if len(stk) == 0 else "NO")
    else:
        # top 操作
        print(stk[-1])

