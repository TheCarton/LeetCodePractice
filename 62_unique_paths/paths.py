class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[1 for _ in range(n)] for _ in range(m)] 
        #todo: reduce space complexity to O(n) from O(n * m)

        for row_i in range(1, m):
            for col_j in range(1, n):
                left = table[row_i][col_j - 1]
                up = table[row_i - 1][col_j]
                table[row_i][col_j] = left + up

        return table[m - 1][n - 1]


s = Solution()

def example_1():
    r = s.uniquePaths(3, 7)
    print(r)
    assert(r == 28)

def example_small():
    r = s.uniquePaths(1, 1)
    print(r)
    assert(r == 1)

example_1()
example_small()
