from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        subarray_max, prev_subarray = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr_subarray = max(nums[i], prev_subarray + nums[i])
            subarray_max = max(subarray_max, curr_subarray)
            prev_subarray = curr_subarray

        return subarray_max


s = Solution()


def example_1():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    r = s.maxSubArray(nums)
    print(r)
    assert (r == 6)


example_1()
