from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 第 k 大元素（保证小根堆只有k个元素）
        heap = []
        for i in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap, nums[i])
            else:
                if nums[i] > heap[0]:
                    heapq.heappush(heap, nums[i])
                    heapq.heappop(heap)

        return heap[0]

