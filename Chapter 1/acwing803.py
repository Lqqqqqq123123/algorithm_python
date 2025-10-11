import sys
input = sys.stdin.readline

n = int(input())

segs = [(0, 0)] * (n + 1)
for i in range(1, n + 1):
    segs[i] = list(map(int, input().split()))

segs[1:] = sorted(segs[1:], key=lambda x: x[0])

res = list()
st, ed = segs[1][0], segs[1][1]

for i in range(2, n + 1):
    if segs[i][0] > ed:
        res.append((st, ed))
        st, ed = segs[i][0], segs[i][1]
    else:
        ed = max(ed, segs[i][1])

res.append((st, ed))

print(len(res))