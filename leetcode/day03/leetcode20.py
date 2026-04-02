class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        s1 = {'(', '{', '['}
        for c in s:
            # 左括号
            if c in s1:
                stk.append(c)
            else:
                if not stk:
                    return False
                top = stk.pop()
                if (top == '(' and c != ')') or (top == '[' and c != ']') or (top == '{' and c != '}'):
                    return False

        return True if not stk else False
