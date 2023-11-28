from typing import List
from itertools import zip_longest


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlap(a: List[int], b: List[int]) -> bool:
            return not (a[1] < b[0] or b[1] < a[0])
        if len(intervals) <= 1:
            return intervals
        mid = len(intervals) // 2
        left = self.merge(intervals[:mid])
        right = self.merge(intervals[mid:])
        ret = []

        for (l, r) in zip_longest(left, right):
            if l is None:
                ret.append(r)
            elif r is None:
                ret.append(l)
            elif overlap(l, r):
                merged_interval = [min(l[0], r[0]), max(l[1], r[1])]
                ret.append(merged_interval)
            else:
                tail = [l, r]
                tail.sort(key=lambda x: (x[0], x[1]))
                ret = ret + tail

        return ret


def main():
    s = Solution()
    ex1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    ret = s.merge(ex1)
    correct = [[1, 6], [8, 10], [15, 18]]
    print(f"{ret}\n{correct}")
    ex2 = [[1,4],[2,3]]
    ret_ex2 = s.merge(ex2)
    cor_ex2 = [[1,4]]
    print(f"{ret_ex2}\n{cor_ex2}")
main()
