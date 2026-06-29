from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        # 1. 先排序
        arr.sort(key=lambda x: x)

        # 2. 逐个元素判断
        for i in range(n):
            if i == 0:
                arr[i] = 1
            else:
                if abs(arr[i - 1] - arr[i]) > 1:
                    arr[i] = arr[i - 1] + 1

        # print(arr)

        return arr[-1]

