from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = curr_max = global_max = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            curr_min, curr_max = min(n, n * curr_min, n * curr_max), max(n, n * curr_min, n * curr_max)
            global_max = max(curr_max, global_max)
        return global_max

s = Solution()

def example_one():
    a = [2,3,-2,4]
    correct = 6
    r = s.maxProduct(a)
    print(f"{correct}")
    print(f"{r}")

def example_two():
    nums = [-2, 0, -1]
    correct = 0
    r = s.maxProduct(nums)
    print(f"{correct}")
    print(f"{r}")

def example_fail_one():
    nums = [-2,3,-4]
    correct = 24
    r = s.maxProduct(nums)
    print(f"{correct}")
    print(f"{r}")

def main():
    example_fail_one()

main()