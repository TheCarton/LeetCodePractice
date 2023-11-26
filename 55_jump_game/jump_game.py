from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_jump = nums[0]
        for i in range(1, len(nums)):
            if curr_jump == 0:
                return False
            curr_jump -= 1
            curr_jump = max(nums[i], curr_jump)

        return True

s = Solution()
def example_1():
    a = [2,3,1,1,4]    
    r = s.canJump(a)
    assert(r)


def example_2():
    a = [3,2,1,0,4]    
    r = s.canJump(a)
    assert(not r)

example_1()
example_2()