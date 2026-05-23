class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        s1 = {'(', '{', '['}
        for c in s:
            if c in s1:
                stk.append(c)
            else:
                if not stk:
                    return False
                if (c == ')' and stk[-1] != '(') or (c == '}' and stk[-1] != '{') or (c == ']' and stk[-1] != '['):
                    return False
                stk.pop()

        return not stk
