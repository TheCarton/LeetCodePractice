from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        intervals.sort()

        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            last_start, last_end = merged[-1]

            if start <= last_end:
                merged[-1] = [last_start, max(end, last_end)]
            else:
                merged.append(intervals[i])

        return merged



s = Solution()

def example_1():
    e1 = [[1,3],[2,6],[8,10],[15,18]]
    c = [[1,6],[8,10],[15,18]]
    r = s.merge(e1)
    print(r)
    print(c)

def fail_1():
    f1 = [[1,4],[0,2],[3,5]]
    r = s.merge(f1)
    c = [[0,5]]
    print(r)
    print(c)

fail_1()