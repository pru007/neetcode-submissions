import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapStones = [-x for x in stones]
        heapq.heapify(heapStones)
        print(heapStones)
        while heapStones:
            if len(heapStones)<2:
                return -heapStones[0]
            stone1 = -heapq.heappop(heapStones)
            stone2 = -heapq.heappop(heapStones)
            remStone = stone1-stone2
            if remStone>0:
                heapq.heappush(heapStones, -remStone)
        # if len(heapStones) == 0:
        return 0