import sys

input = sys.stdin.readline

class DLinkedList:
    def __init__(self, n=100010):
        self.e = [0] * n
        self.l = [0] * n
        self.r = [0] * n
        self.idx = 2
        self.r[0] = 1; self.l[1] = 0
        self.l[0] = -1; self.r[1] = -1

    

    def add_k_right(self, k:int, x:int):
        self.e[self.idx] = x
        self.r[self.idx] = self.r[k]
        self.l[self.idx] = k
        self.l[self.r[k]] = self.idx
        self.r[k] = self.idx
        self.idx += 1
    
    def remove(self, k:int):
        self.r[self.l[k]] = self.r[k]
        self.l[self.r[k]] = self.l[k]
    


# 初始化链表
dll = DLinkedList()

m = int(input())

for i in range(m):
    lines = input().split()
    if lines[0] == 'L':
        dll.add_k_right(0, int(lines[1]))
    elif lines[0] == 'R':
        dll.add_k_right(dll.l[1], int(lines[1]))
    elif lines[0] == 'D':
        dll.remove(int(lines[1]) + 1)
    elif lines[0] == 'IL':
        dll.add_k_right(dll.l[int(lines[1]) + 1], int(lines[2]))
    elif lines[0] == 'IR':
        dll.add_k_right(int(lines[1]) + 1, int(lines[2]))
    

head = dll.r[0]
while head != 1:
    print(dll.e[head], end=' ')
    head = dll.r[head]

