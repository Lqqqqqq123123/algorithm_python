# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from torch.distributed.rpc.internal import deserialize


class Solution:


    def deserialize(self, s: str) -> NestedInteger:
        u = 0
        def dfs() -> NestedInteger:
            nonlocal u

            # 两种情况，要么是一个整数，要么是一个列表
            if s[u] == '[':
                res = NestedInteger()
                u += 1
                while u < len(s) and s[u] != ']':
                    res.add(dfs())

                    if u < len(s) and s[u] == ',':
                        u += 1 # 跳过逗号，继续处理

                u += 1 # 跳过右括号
                return res

            else:
                # 当前是一个整数
                start, st = u, False
                if s[u] == '-':
                    st = True
                    u += 1

                while u < len(s) and s[u].isdigit():
                    u += 1

                # u就是这个数的下一个位置

                val = int(s[start:u])
                if st:
                    val = -val

                return NestedInteger(val)



        return dfs()






