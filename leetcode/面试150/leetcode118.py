from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            else:
                pre = i - 1
                temp = []
                for j in range(i + 1):
                    left = res[pre][j - 1] if j - 1 >= 0 else 0
                    right = res[pre][j] if j <= pre else 0
                    temp.append(left + right)

                res.append(temp)

        return res