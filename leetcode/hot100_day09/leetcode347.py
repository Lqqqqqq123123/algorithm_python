from typing import List, Optional
import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1


        heap = []
        for i in dic:
            heapq.heappush(heap, (dic[i], i))
            # 堆的大小大于k时，弹出堆顶元素（也就是把那个频率最小的元素弹出）
            if len(heap) > k:
                heapq.heappop(heap)

        return [item[1] for item in heap]
    



