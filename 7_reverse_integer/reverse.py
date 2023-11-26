class Solution:
    def reverse(self, x: int) -> int:
        rev_n = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        while x > 0:
            digit = x % 10
            rev_n = (rev_n + digit)
            x = (x - digit) // 10
            if x > 0:
                rev_n *= 10

        return sign * rev_n

s = Solution()

def example_1():
    r = s.reverse(123)
    print(r)
    assert(r == 321)


def example_2():
    r = s.reverse(-123)
    print(r)
    assert(r == -321)

example_2()
