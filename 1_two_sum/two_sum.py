from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = dict()
        for (i, n) in enumerate(nums):
            if n in compliments:
                return [i, compliments[n]]
            comp = target - n
            compliments[comp] = i

        assert False


s = Solution()

def example_1():
    n = [2,7,11,15]
    r = s.twoSum(n, 9)
    print(r)

example_1()
