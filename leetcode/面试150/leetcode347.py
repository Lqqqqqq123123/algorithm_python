from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        heap = []

        for num, times in dic.items():
            heapq.heappush(heap, (times, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for times, num in heap]
    