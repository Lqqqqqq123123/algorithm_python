from typing import List
class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        res, u = '', 0
        # 解码一个 []
        def dfs():
            nonlocal u, res
            temp = ''
            while u < n and s[u] != ']':
                if s[u].isdigit():
                    times = 0
                    while u < n and s[u].isdigit():
                        # 提取这个数字
                        times = times * 10 + int(s[u])
                        u += 1

                    # 跳过左括号
                    u += 1
                    sub_str = dfs()
                    # 跳过右括号
                    u += 1
                    temp += times * sub_str
                else:
                    temp += s[u]
                    u += 1

            return temp

        return dfs()

