from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            else:
                pre = i - 1
                line = []
                for j in range(i + 1):  # 第 i 行，有 i + 1 个元素
                    # temp 是左上方 + 正上方
                    left = res[pre][j - 1] if j - 1 >= 0 else 0
                    up = res[pre][j] if j <= i - 1 else 0
                    line.append(left + up)

                res.append(line)

        return res
