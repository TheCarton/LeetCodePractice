class Solution:
    def countPrimes(self, n: int) -> int:
        primes = []
        for i in range(2, n):
            if not any(map(lambda n: i % n == 0, primes)):
                primes.append(i)

        return len(primes)

    def countPrimes2(self, n):
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return sum(primes)
        

s = Solution()
def example_1():
    n = s.countPrimes2(10)
    print(f"{n}")

def main():
    example_1()

main()
         