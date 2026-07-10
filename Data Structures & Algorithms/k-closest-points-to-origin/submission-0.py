import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            heapq.heappush(heap,(math.sqrt(points[i][0]**2+points[i][1]**2),i,
            {"x":points[i][0],"y":points[i][1]}))
        results = []
        for j in range(k):
            res = heapq.heappop(heap)
            results.append([res[2]['x'],res[2]['y']])
        return results

        # distance = [math.sqrt(points[i][0]**2+points[i][1]**2) for i in range(len(points))]
