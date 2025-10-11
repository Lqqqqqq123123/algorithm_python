import sys
input = sys.stdin.readline

class LinkedList:
    def __init__(self, n=100010):
        self.e = [0] * n
        self.ne = [0] * n
        self.h = -1
        self.idx = 0
    
    def add_head(self, x:int):
        self.e[self.idx] = x
        self.ne[self.idx] = self.h
        self.h = self.idx
        self.idx += 1
    
    def add(self, k:int, x:int):
        self.e[self.idx] = x
        self.ne[self.idx] = self.ne[k]
        self.ne[k] = self.idx
        self.idx += 1
    
    def remove(self, k:int):
        self.ne[k] = self.ne[self.ne[k]]

m = int(input())
ll = LinkedList()

for i in range(m):
    lines = input().split()
    if lines[0] == "H":
        ll.add_head(int(lines[1]))
    elif lines[0] == "D":
        k = int(lines[1])
        if k == 0: ll.h = ll.ne[ll.h]
        else: ll.remove(k - 1)
    else:
        k, x = int(lines[1]), int(lines[2])
        ll.add(k - 1, x)
    

while ll.h != -1:
    print(ll.e[ll.h], end=' ')
    ll.h = ll.ne[ll.h]