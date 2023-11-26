from typing import List


class NumString:
    def __init__(self, n):
        self.n = n

    def __lt__(self, other):
        a = int(str(self.n) + str(other.n))
        b = int(str(other.n) + str(self.n))
        return a < b

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_strings = [NumString(n) for n in nums]
        num_strings.sort(reverse=True)
        return ''.join(str(num_string.n) for num_string in num_strings)

       


s = Solution()


def example_1():
    nums = [3, 30, 34, 5, 9]
    corr = "9534330"
    r = s.largestNumber(nums)
    print(f"corr={corr}\nret ={r}")



def main():
    example_1()


main()
