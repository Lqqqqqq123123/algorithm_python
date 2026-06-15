import heapq
import math
class MedianFinder:

    def __init__(self):
        self.h1 = []
        self.h2 = []

    @property
    def n1(self):
        return len(self.h1)

    @property
    def n2(self):
        return len(self.h2)

    def addNum(self, num: int) -> None:
        # 如果第一个堆元素为空或者新加入的元素小于第一个堆的元素，则加入第一个堆
        if self.n1 == 0 or num < -self.h1[0]:
            heapq.heappush(self.h1, -num)

            # 判断，如果当前 len(h1) > len(h2) + 1
            if self.n1 > self.n2 + 1:
                x = heapq.heappop(self.h1)
                heapq.heappush(self.h2, -x)
        else:
            heapq.heappush(self.h2, num)
            # 判断，如果当前 len(h2) > len(h1)
            if self.n2 > self.n1:
                x = heapq.heappop(self.h2)
                heapq.heappush(self.h1, -x)


    def findMedian(self) -> float:
        if self.n1 == self.n2:
            return (-self.h1[0] + self.h2[0]) / 2
        else:
            return -self.h1[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()