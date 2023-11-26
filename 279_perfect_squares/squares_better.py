class Solution:
    def numSqures(self, n: int) -> int:
        squares = [i for i in range(n + 1)]

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                squares[target] = min(squares[target], 1 + squares[target - square])
