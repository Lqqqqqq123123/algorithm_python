import heapq
class MedianFinder:

    def __init__(self):
        # 两个堆
        self.h1 = []
        self.h2 = []

    @property
    def n1(self):
        return len(self.h1)

    @property
    def n2(self):
        return len(self.h2)

    def addNum(self, num: int) -> None:
        if not self.h1:
            heapq.heappush(self.h1, -num)
        elif num < -self.h1[0]:
            heapq.heappush(self.h1, -num)
            if self.n1 > self.n2 + 1:
                # 数量超了
                temp = -heapq.heappop(self.h1)
                heapq.heappush(self.h2, temp)
        else:
            heapq.heappush(self.h2, num)
            if self.n2 > self.n1:
                temp = heapq.heappop(self.h2)
                heapq.heappush(self.h1, -temp)


    def findMedian(self) -> float:
        if self.n1 == self.n2:
            return (-self.h1[0] + self.h2[0]) / 2
        else:
            return -self.h1[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()