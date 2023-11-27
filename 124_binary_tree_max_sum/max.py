# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = [root.val]

        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            left_val = max(dfs(node.left), 0)
            right_val = max(dfs(node.right), 0)
            thru_val = left_val + node.val + right_val
            max_path[0] = max(max_path[0], thru_val)
            return node.val + max(left_val, right_val)

        dfs(root)
        return max_path[0]


s = Solution()


def example_2():
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    r = s.maxPathSum(root)
    print(r)
    assert (r == 42)


example_2()
