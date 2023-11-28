from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = 0
        sum = 0
        for n in nums:
            sum += n
            ret = max(ret, sum)
            sum = max(sum, 0)
          
        return ret