from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n_pos = 0
        for i in range(len(nums)):
            if not 1 <= nums[i] <= len(nums):
                nums[i] = len(nums) + 1
            else:
                n_pos += 1

        for i in range(len(nums)):
            v = abs(nums[i])
            if 1 <= v <= len(nums):
                if nums[v - 1] > 0:
                    nums[v - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1


s = Solution()        


def example_2():
    nums = [3,4,-1,1]
    r = s.firstMissingPositive(nums)
    print(r)
    assert(r == 2)

def example_4():
    nums = [1]
    r = s.firstMissingPositive(nums)
    print(r)
    assert(r == 2)

example_2()
example_4()
