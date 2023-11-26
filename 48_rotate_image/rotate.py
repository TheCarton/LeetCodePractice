from collections import deque
from typing import List
from itertools import cycle


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                top_left = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]

                matrix[bottom - i][left] = matrix[bottom][right - i]

                matrix[bottom][right - i] = matrix[top + i][right]

                matrix[top + i][right] = top_left
            left += 1
            right -= 1

s = Solution()


def example_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"{matrix}")
    s.rotate(matrix)
    print(f"{matrix}")


def main():
    example_1()


main()
