class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        last_row = [1 for _ in range(n)]

        for _ in range(m - 1):
            new_row = [1]
            for i in range(1, n):
                new_row.append(new_row[-1] + last_row[i])
            last_row = new_row

        return last_row[-1]


s = Solution()

def example_1():
    r = s.uniquePaths(3, 7)
    assert(r == 28)

example_1()
               
