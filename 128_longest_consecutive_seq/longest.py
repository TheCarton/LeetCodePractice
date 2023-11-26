class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_length = 0
        for n in nums:
            is_sequence_start = not (n - 1 in numSet)
            if is_sequence_start:
                next_num = n + 1
                length = 1
                while next_num in numSet:
                    next_num += 1
                    length += 1
                max_length = max(max_length, length)
        
        return max_length
                    
                