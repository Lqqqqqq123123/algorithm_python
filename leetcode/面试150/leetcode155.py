class MinStack:

    class Node:
        def __init__(self, val, min_val):
            self.val = val
            self.min_val = min_val

    def __init__(self):
        self.stk = []

    def push(self, value: int) -> None:
        if not self.stk:
            self.stk.append(self.Node(value, value))
        else:
            self.stk.append(self.Node(value, min(value, self.stk[-1].min_val)))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1].val

    def getMin(self) -> int:
        return self.stk[-1].min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()