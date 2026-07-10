from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)
        heap = []
        result = []
        for num, count in countMap.items():
            heapq.heappush(heap, (-count, num))
        for i in range(k):
            count, num = heapq.heappop(heap)
            result.append(num)
        return result