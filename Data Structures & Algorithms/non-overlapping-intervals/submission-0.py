class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])       # sort by END time
        removals = 0
        prev_end = intervals[0][1]               # end of last kept interval

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= prev_end:                # no overlap → keep it
                prev_end = end
            else:                                # overlaps → remove this one
                removals += 1
        return removals