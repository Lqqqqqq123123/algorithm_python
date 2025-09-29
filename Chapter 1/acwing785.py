import sys

#
def quick_sort(a: list, l: int, r: int):
   if l >= r:
       return

   i, j, pivot = l - 1, r + 1, a[(l + r) >> 1]

   while i < j:
       i, j = i + 1, j - 1
       while a[i] < pivot: i += 1
       while a[j] > pivot: j -= 1
       if i < j: a[i], a[j] = a[j], a[i]

   quick_sort(a, l, j)
   quick_sort(a, j + 1, r)


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    quick_sort(a, 0, len(a) - 1)
    for i in range(len(a)):
        print(a[i], end=' ')
