class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i for i in range(n + 1)]

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if square > target:
                    break
                remainder = target - square
                squares[target] = min(squares[target], 1 + squares[remainder])

        return squares[n]

s = Solution()
def example_1():
    r = s.numSquares(12)
    print(r)
    assert(r == 3)

def example_2():
    r = s.numSquares(13)
    print(r)
    assert(r == 2)

example_1()
example_2()