from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(index: int):
            if index >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
            dfs(index + 1)

        dfs(0)
        return res


def main():
    s = Solution()
    ex1 = [1,2,3]
    correct_ex1 = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    ret_ex1 = s.subsets(ex1)
    print(f"{ret_ex1}\n{correct_ex1}")

main()