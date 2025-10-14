# 字符串哈希

P = 131 # 看作一个 p 进制的数
mod = int(1e9 + 7)
n, m = map(int, input().split())

s = " " + input().strip() # 下标从1开始

h, p = [0] * (n + 1), [1] * (n + 1)

# 预处理前缀和
for i in range(1, n + 1):
    h[i] = (h[i - 1] * P + ord(s[i]) - ord('0')) % mod
    p[i] = p[i - 1] * P % mod

# 计算子串哈希值
def get(l: int, r: int) -> int:
    return (h[r] - h[l - 1] * p[r - l + 1]) % mod


for _ in range(m):
    l1, r1, l2, r2 = map(int, input().split())
    if get(l1, r1) == get(l2, r2):
        print("Yes")
    else:
        print("No")