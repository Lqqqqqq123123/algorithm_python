# acwing 799
import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
def main1():
   

    # 记录区间里面每个元素出现的个数
    cnt = [0] * (int(1e5 * 10))

    i, j, res = 0, 0, 1

    while i < n:
        cnt[arr[i]] += 1
        while cnt[arr[i]] > 1:
            cnt[arr[j]] -= 1
            j += 1

        res = max(res, i - j + 1)

    print(res)


def main2():
    cnt = defaultdict(int)
    i, j, res = 0, 0, 1

    for i in range(n):
        cnt[arr[i]] += 1

        while(cnt[arr[i]] > 1):
            cnt[arr[j]] -= 1
            j += 1
        
        res = max(res, i - j + 1)
    
    print(res)

main2()