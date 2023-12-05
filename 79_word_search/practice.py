class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid_coords(col: int, row: int) -> bool:
            return col >= 0 and col < len(board[0]) and row >= 0 and row < len(board)
        def dfs(col: int, row: int, i: int) -> bool:
            if not valid_coords(col, row) or board[row][col] != word[i]:
                return False
            i += 1
            if i == len(word):
                return True 
            used_char = board[row][col]
            board[row][col] = '!'
            word_found = (dfs(col + 1, row, i) or
                          dfs(col - 1, row, i) or
                          dfs(col, row + 1, i) or
                          dfs(col, row - 1, i))
            if word_found:
                return True
            board[row][col] = used_char
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(col, row, 0):
                    return True

        return False
