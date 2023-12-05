# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = dict()
        node = head

        dummy_copy = Node(0)
        prev_copy = dummy_copy
        while node:
            new_node = Node(node.val)
            prev_copy.next = new_node
            map[node] = new_node

            prev_copy = new_node
            node = node.next

        node = head
        while node:
            if node.random:
                map[node].random = map[node.random]
            node = node.next

        return dummy_copy.next
            

