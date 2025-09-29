# acwing795：一维前缀和

n, m = map(int, input().split())
arr = list(n + 1)


for i in range(1, n + 1):
    arr[i] += arr[i - 1]

def get_sum(l, r) -> int:
    return arr[r] - arr[l - 1]

for i in range(m):
    l, r = map(int, input().split())
    print(get_sum(l, r))

