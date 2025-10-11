import sys
input = sys.stdin.readline

h = -1
e, ne, idx = [0] * (100010), [0] * (100010), 0

def add_head(x:int):
    global idx, h
    e[idx] = x; ne[idx] = h; h = idx; idx += 1

def add(k:int, x:int):
    global idx
    e[idx] = x; ne[idx] = ne[k]; ne[k] = idx; idx += 1

def remove(k:int):
    ne[k] = ne[ne[k]]


m = int(input())

for i in range(m):
    lines = input().split()
    if lines[0] == "H":
        add_head(int(lines[1]))
    elif lines[0] == "D":
        k = int(lines[1])
        if k == 0: h = ne[h]
        else: remove(k - 1)
    else:
        k, x = int(lines[1]), int(lines[2])
        add(k - 1, x)
    

while h != -1:
    print(e[h], end=' ')
    h = ne[h]