"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr_node = root
        next_node = root.left if root else None
        while curr_node and next_node:
            curr_node.left.next = curr_node.right

            if curr_node.next:
                curr_node.right.next = curr_node.next.left

            curr_node = curr_node.next
            if not curr_node:
                curr_node = next_node
                next_node = curr_node.left

        return root
        
      
        