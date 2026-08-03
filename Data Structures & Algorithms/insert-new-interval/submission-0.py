class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        newStart, newEnd = newInterval

        # Phase 1: intervals entirely before newInterval
        while i < n and intervals[i][1] < newStart:
            res.append(intervals[i])
            i += 1

        # Phase 2: overlapping intervals — absorb into newInterval
        while i < n and intervals[i][0] <= newEnd:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1
        res.append([newStart, newEnd])       # emit the merged interval once

        # Phase 3: intervals entirely after newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res