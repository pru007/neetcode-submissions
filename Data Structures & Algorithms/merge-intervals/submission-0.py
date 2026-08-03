class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort()
        for start, end in intervals:
            if not merged or start>merged[-1][1]:
                merged.append([start,end])
            else:
                merged[-1][1] = max(merged[-1][1],end)
        return merged