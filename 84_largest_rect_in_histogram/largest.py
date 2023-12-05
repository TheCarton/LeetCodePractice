from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        return max_area
            



s = Solution()


def example_1():
    h = [2, 1, 5, 6, 2, 3]
    r = s.largestRectangleArea(h)
    assert (r == 10)


example_1()
