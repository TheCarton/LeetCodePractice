from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for i in range(1, numRows):
            new_row = [1]
            for j in range(len(triangle[i - 1]) - 1):
                left = triangle[i - 1][j]
                right = triangle[i - 1][j + 1]
                new_row.append(left + right)

            new_row.append(1)
            triangle.append(new_row)

        return triangle


s = Solution()


def example_1():
    r = s.generate(5)
    c = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    assert(all(x == y for x, y in zip(r, c)))
    print(r)


def example_2():
    r = s.generate(1)
    c = [[1]]
    assert(all(x == y for x, y in zip(r, c)))
    print(r)

example_1()
example_2()
