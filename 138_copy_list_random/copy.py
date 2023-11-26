# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        map = dict()
        node = head
        while node:
            copy = Node(node.val)
            map[node] = copy
            node = node.next

        node = head
        while node:
            copy = map[node]
            if node.next in map:
                copy.next = map[node.next]
            if node.random in map:
                copy.random = map[node.random]
            node = node.next

        return map[head]           