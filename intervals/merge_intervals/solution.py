from typing import List

class MergeIntervalsSolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        sorted_intervals = sorted(intervals, key=lambda item: item[0])
        merged = [sorted_intervals[0][:]]

        for start, end in sorted_intervals[1:]:
            last = merged[-1]
            if start <= last[1]:
                last[1] = max(last[1], end)
            else:
                merged.append([start, end])

        return merged
