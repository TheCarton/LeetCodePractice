# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def append_from_left(node: TreeNode, level: List[TreeNode]):
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)

        def append_from_right(node: TreeNode, level: List[TreeNode]):
            if node.right:
                level.append(node.right)
            if node.left:
                level.append(node.left)

        level_order = []
        stack = [[root]]
        right_order = True
        while stack:
            level = stack.pop()
            level_order.append([node.val for node in level])
            next_level = []

            for i in reversed(range(len(level))):
                node = level[i]
                if right_order:
                    append_from_right(node, next_level)
                else:
                    append_from_left(node, next_level)

            right_order = not right_order
            if next_level:
                stack.append(next_level)

        return level_order


s = Solution()


def example_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    r = s.zigzagLevelOrder(root)
    c = [[3], [20, 9], [15, 7]]
    print("r = ", r)
    print("c = ", c)


def fail():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    r = s.zigzagLevelOrder(root)
    c = [[1], [3, 2], [4, 5]]
    print("r = ", r)
    print("c = ", c)


example_1()
fail()
