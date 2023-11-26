class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max( (v, i) for i, v in enumerate(nums) ) [1]
        middle = len(nums) // 2
        left = middle - 1
        right = middle + 1
        while 0 <= middle < len(nums):
            left_n = nums[left] if left >= 0 else float("-inf")
            middle_n = nums[middle]
            right_n = nums[right] if right < len(nums) else float("-inf")
            if left_n > middle_n:
                middle = left
                right = middle + 1
                left = middle - 1
            elif right_n > middle_n:
                middle = right
                right = middle + 1
                left = middle - 1
            else:
                return middle

        raise ValueError("Invalid inputs")