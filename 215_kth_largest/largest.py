from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return nums[0]
        k_largest_indices = set()
        curr_max, curr_max_index, last_max = float("-inf"), None, float("-inf")
        while len(k_largest_indices) < k:
            for i in range(len(nums)):
                n = nums[i]
                if n >= curr_max and i not in k_largest_indices:
                    curr_max, curr_max_index = n, i
            k_largest_indices.add(curr_max_index)
            last_max = curr_max
            curr_max, curr_max_index = float("-inf"), None
        return last_max
    
s = Solution()

def example_fail():
    a = [2, 1]
    r = s.findKthLargest(a, 2)
    print("1")
    print(r)



def example_2():
    a = [3,2,3,1,2,4,5,5,6]
    r = s.findKthLargest(a, 4)
    print("4")
    print(r)

example_fail()
example_2()