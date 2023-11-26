# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return BSTRecur(root, -math.inf, math.inf)

    def BSTRecur(node, minBound, maxBound) -> bool:
        if not node:
            return True
        if node.val < minBound or node.val > maxBound:
            return False 
        if not BSTRecur(node.left, node.val, maxBound):
            return False
        if not BSTRecur(node.right, minBound, node.val):
            return False
        return True
        
        