from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1

        offset = 0
        for color, count in enumerate(counts):
            for i in range(count):
                nums[i + offset] = color
            offset += count



s = Solution()

def example_1():
    nums = [2,0,2,1,1,0]
    correct = [0,0,1,1,2,2]
    s.sortColors(nums)
    print(f"{nums}\n{correct}")

def main():
    example_1()

main()