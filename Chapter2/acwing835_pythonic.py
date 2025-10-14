# Python 版本 Tire树

import sys
input = sys.stdin.readline
prt = sys.stdout.write

class TireNode:
    def __init__(self):
        self.son = {}
        self.cnt = 0
    

root = TireNode()

def insert(s : str):
    p = root
    for c in s:
        if c not in p.son:
            p.son[c] = TireNode()
        p = p.son[c]
    p.cnt += 1


def query(s : str) -> int:
    p = root
    for c in s:
        if c not in p.son: return 0
        p = p.son[c]
    return p.cnt


n = int(input())

for i in range(n):
    op, s = input().split()
    if op == "I":
        insert(s)
    else:
        prt(str(query(s)) + "\n")
        