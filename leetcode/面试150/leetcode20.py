class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stk = []
        lefts = {'(', '[', '{'}

        for c in range(n):
            if c in lefts:
                stk.append(c)
            else:
                if not stk:
                    return False
                top = stk.pop()
                if (c == ')' and top != '(') or (c == ']' and top != '[') or (c == '}' and top != '{'):
                    return False


        return not stk