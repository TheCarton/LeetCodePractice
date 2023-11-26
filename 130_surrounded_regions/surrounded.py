from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        last_row_i = len(board) - 1
        for i in range(len(board[0])):
            if board[0][i] == "O":
                self.flip_touching((0, i), board)
            if board[last_row_i][i] == "O":
                self.flip_touching((last_row_i, i), board)

        for row_i in range(len(board)):
            if board[row_i][0] == "O":
                self.flip_touching((row_i, 0), board)
            last_elem_i = len(board[row_i]) - 1
            if board[row_i][last_elem_i] == "O":
                self.flip_touching((row_i, last_elem_i), board)

        for row_i in range(len(board)):
            for j in range(len(board[row_i])):
                if board[row_i][j] == "N":
                    board[row_i][j] = "O"
                else:
                    board[row_i][j] = "X"

    def flip_touching(self, square: (int, int), board: List[List[str]]) -> None:
        board[square[0]][square[1]] = "N"
        directions = []
        for offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            row = offset[0] + square[0]
            col = offset[1] + square[1]
            valid = (0 <= row <= len(board) - 1) and (0 <= col <= len(board[0]) - 1)
            if valid:
                directions.append((row, col))

        for dir in directions:
            if board[dir[0]][dir[1]] == "O":
                self.flip_touching(dir, board)
s = Solution()
def example_1():
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]     
    correct = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    s.solve(board)
    print(f"{board}")
    print(f"{correct}")

def main():
    example_1()

main()