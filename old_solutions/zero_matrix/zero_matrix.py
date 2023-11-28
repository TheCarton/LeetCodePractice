from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zeroed = False
        first_col_zeroed = False

        def zeroRow(row_index):
            for i in range(len(matrix[row_index])):
                matrix[row_index][i] = 0

        def zeroCol(col_index):
            for row in matrix:
                row[col_index] = 0

        for row_index, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == 0:
                    first_row_zeroed = first_row_zeroed or row_index == 0
                    first_col_zeroed = first_col_zeroed or j == 0
                    if row_index > 0:
                        matrix[row_index][0] = 0
                    if j > 0:
                        matrix[0][j] = 0

        for i, value in enumerate(matrix[0]):
            if i == 0:
                continue
            if value == 0:
                zeroCol(i)

        for j, row in enumerate(matrix):
            if row[0] == 0:
                zeroRow(j)

        if first_row_zeroed:
            zeroRow(0)
        if first_col_zeroed:
            zeroCol(0)


def main():
    s = Solution()
    ex1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes(ex1)
    ex1_ans = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print(f"{ex1}\n{ex1_ans}")

    ex2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    ex2_ans = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    s.setZeroes(ex2)

    print(f"{ex2}\n{ex2_ans}")


if __name__ == "__main__":
    main()
