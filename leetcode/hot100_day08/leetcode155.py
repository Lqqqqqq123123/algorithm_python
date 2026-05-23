class MinStack:

    class Node:
        def __init__(self, val, min_val):
            self.val = val
            self.min = min_val

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append(self.Node(val, val))
        else:
            self.stk.append(self.Node(val, min(val, self.stk[-1].min)))


    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1].val

    def getMin(self) -> int:
        return self.stk[-1].min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()