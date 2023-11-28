from typing import List
from itertools import cycle
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        col_n = len(matrix[0])
        visit_cols = col_n + 2
        row_n = len(matrix)
        visit_rows = row_n + 2
        
        def left(i: tuple) -> tuple:
            return i[0], i[1] - 1
        def right(i) -> tuple:
            return i[0], i[1] + 1
        def up(i) -> tuple:
            return i[0] - 1, i[1]
        def down(i) -> tuple:
            return i[0] + 1, i[1]

        def visit_index(i) -> tuple:
            return i[0] + 1, i[1] + 1

        visit = [[False for _ in range(visit_cols)] for _ in range(visit_rows)]                
        for visit_row in visit[1:visit_rows - 1]:
            for i in range(1, len(visit_row) - 1):
                visit_row[i] = True

        ret = []
        directions = cycle([right, down, left, up])
        direction = next(directions)
        i = (0, 0)
        while len(ret) < row_n * col_n:
            ret.append(matrix[i[0]][i[1]])
            j = visit_index(i)
            visit[j[0]][j[1]] = False

            next_j = visit_index(direction(i))
            if not visit[next_j[0]][next_j[1]]:
                direction = next(directions)
            i = direction(i)

        return ret
                           

            

            
        
def main():
    s = Solution()
    r = s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
    correct = [1,2,3,6,9,8,7,4,5]
    print(f"{r}")
    print(f"{correct}")

main()