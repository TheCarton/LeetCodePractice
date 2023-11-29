from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        k = 1
        for i in range(1, len(nums)):
            if nums[k - 1] != nums[i]:
                nums[k] = nums[i]
                k += 1

        return k


s = Solution()

def example_2():
    nums = [0,0,1,1,1,2,2,3,3,4]
    r = s.removeDuplicates(nums)
    assert(r == 5)
    print(nums)

example_2()
