from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subset_recur(nums)

    def subset_recur(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        subsets = self.subset_recur(nums[:len(nums) - 1])

def main():
    s = Solution()
    
    ex1 = [1,2,3]
    ret_ex1 = s.subsets(ex1)
    ans_ex1 = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]                
    print(f"{ret_ex1}\n{ans_ex1}")

main()
    