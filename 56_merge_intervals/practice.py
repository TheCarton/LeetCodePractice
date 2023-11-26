from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            last_start, last_end = merged[-1]
            start, end = intervals[i]

            if start <= last_end:
                merged[-1] = [last_start, max(last_end, end)]
            else:
                merged.append([start, end])

        return merged
