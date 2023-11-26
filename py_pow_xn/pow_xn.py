




class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = abs(n)
        res = 1
        while n:
            if n % 2:
                res *= x
            x *= x
            n = n // 2 
        return res
def main():
    s = Solution()
    pairs = [(3,5), (2, -3), (-2, 2), (2, 10)]
    for pair in pairs:
        a = pair[0]
        b = pair[1]
        true = a ** b
        res = s.myPow(a, b)
        correct = true == res
        if not correct:
            print("test failed on x = ", a, "n = ", b)
            print("expected ", true)
            print("got ", res)










if __name__ == "__main__":
    main()