# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def builder(left: int, right: int):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = builder(left, mid - 1)
            node.right = builder(mid + 1, right)
            return node

        return builder(0, len(nums) - 1)


s = Solution()


def example_1():
    nums = [-10, -3, 0, 5, 9]
    r = s.sortedArrayToBST(nums)


example_1()
