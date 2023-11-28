from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_left(left: int, right: int, mid: int) -> (int, int):
            right = mid - 1
            return left, right
        def search_right(left: int, right: int, mid: int) -> (int, int):
            left = mid + 1
            return left, right
        left = self.binarySearchRange(nums, target, search_left)
        if left >= 0:
            right = self.binarySearchRange(nums, target, search_right)
            return [left, right]
        else:
            return [-1, -1]

    def binarySearchRange(self, nums: List[int], target: int, on_equals) -> int:
        left = 0
        right = len(nums) - 1
        target_index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                target_index = mid
                left, right = on_equals(left, right, mid)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return target_index

s = Solution()

def example_one():
    a = [5,7,7,8,8,10]
    r = s.searchRange(a, 8)
    assert(r == [3, 4])

def main():
    example_one()

main()
    
        


            
