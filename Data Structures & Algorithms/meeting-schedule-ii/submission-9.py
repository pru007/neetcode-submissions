"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x:x.start)
        heap = []                                    # end times of occupied rooms
        for iv in intervals:                         # already sorted by start
            if heap and heap[0] <= iv.start:
                heapq.heappop(heap)                  # earliest room freed → reuse
            heapq.heappush(heap, iv.end)
        return len(heap)
                