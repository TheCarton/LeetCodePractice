class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in nums]
        prefix = 1
        for i in range(len(nums)): # compute the exclusive prefix array
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1 # could reuse prefix instead
        for j in reversed(range(len(nums))): # computer the exclusive postfix array
            output[j] *= postfix
            postfix *= nums[j]
        return output
