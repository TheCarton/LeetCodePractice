from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []

        def backtrack(perms):

            if len(perms) == 0:
                res.append(curr.copy())
                return
            
            for i in range(len(perms)):
                curr.append(perms[i])
                backtrack(perms[:i] + perms[i+1:])
                curr.pop()

        backtrack(nums)
        return res        




s = Solution()

def example_one():
    nums = [1, 2, 3]
    r = s.permute(nums)
    print(f"{r}")

def main():
    example_one()

main()


           