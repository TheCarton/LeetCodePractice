from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid_index(col, row) -> bool:
            return col >= 0 and col < len(board[0]) and row >= 0 and row < len(board)
        def dfs(col, row, index) -> bool:
            if not valid_index(col, row) or board[row][col] != word[index]:
                return False
            index += 1
            if index == len(word):
                return True
            used_char = board[row][col]
            board[row][col] = "#"
            word_found = (dfs(col + 1, row, index) or 
                         dfs(col - 1, row, index) or
                         dfs(col, row + 1, index) or
                         dfs(col, row - 1, index))
            if word_found:
                return True
            board[row][col] = used_char
            return False


        for row_j in range(len(board)):
            for col_i in range(len(board[row_j])):
                if dfs(col_i, row_j, 0):
                    return True

        return False


s = Solution()

def example_1():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    r = s.exist(board, word)
    assert(r)

example_1()
