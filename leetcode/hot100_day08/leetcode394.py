from typing import List, Optional
class Solution:
    def decodeString(self, s: str) -> str:
        u = 0
        # 处理一个[]
        def dfs() -> str:
            nonlocal u
            res = [] # 当前层结果
            while u < len(s) and s[u] != ']':
                if s[u].isdigit():
                    # 拿到这个数字
                    t = 0
                    while u < len(s) and s[u].isdigit():
                        t = t * 10 + int(s[u])
                        u += 1

                    # 跳过左括号
                    u += 1
                    # 递归处理这个[]
                    sub_str = dfs()
                    # 跳过右括号
                    u += 1
                    res.append(t * sub_str)

                else:
                    res.append(s[u])

            return ''.join(res)

        return dfs()


