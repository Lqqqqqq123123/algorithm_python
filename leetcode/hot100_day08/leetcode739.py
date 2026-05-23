from typing import List, Optionals

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk, ans = [], [0] * n

        for i in range(n - 1, -1, -1):
            # 栈非空且当前温度大于栈顶元素
            while stk and temperatures[i] >= temperatures[stk[-1]]:
                stk.pop()
            ans[i] = stk[-1] if stk else 0

            stk.append(i)

        return ans
