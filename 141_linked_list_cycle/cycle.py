# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0)
        node = head
        while node:
            next_node = node.next
            if next_node is dummy:
                return True
            node.next = dummy
            node = next_node

        return False
