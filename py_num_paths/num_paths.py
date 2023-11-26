class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = dict({(0, 0): 1})
        for i in range(n):
            for j in range(m):
                current = (i, j)
                if current == (0, 0):
                    continue
                num_paths = 0
                left = (i - 1, j)
                up = (i, j - 1)
                if left in table:
                    num_paths += table.get(left)
                if up in table:
                    num_paths += table.get(up)
                table.update({current: num_paths})
        return table[(n - 1, m - 1)]




def main():
    s = Solution()
    print(f"(3, 7) = {s.uniquePaths(3, 7)}")
    print(f"(23, 12) = {s.uniquePaths(23, 12)}")

main()