class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 1:
            return 0
        n_zeroes = 0
        factor_5 = 5
        n = n // factor_5
        while n > 0:
            n_zeroes += 1
            n = n // factor_5
            factor_5 *= factor_5
        return n_zeroes


s = Solution()

def fac_5():
    r = s.trailingZeroes(5)
    c = 1
    print(c)
    print(r)
    assert(r == c)


fac_5()
