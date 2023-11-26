class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            new_sum = max(n, n + prev_sum)
            max_sum = max(new_sum, max_sum)
            prev_sum = new_sum
        return max_sum