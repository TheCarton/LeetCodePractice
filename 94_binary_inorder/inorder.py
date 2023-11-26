# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []

        def helper(node: TreeNode):
            if node is None:
                return
            helper(node.left)
            traversal.append(node.val)
            helper(node.right)

        helper(root)
        return traversal
