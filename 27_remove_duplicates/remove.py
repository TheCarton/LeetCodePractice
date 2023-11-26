from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        left = 0
        k = 1
        for right in range(1, len(nums)): 
            if nums[left] != nums[right]:
                nums[left + 1] = nums[right]
                left += 1
                k += 1

        return k

s = Solution()

def example_1():
    n = [1,1,2]
    r = s.removeDuplicates(n)
    print(n)
    print("k = ", r)
    assert(r == 2)

example_1()
