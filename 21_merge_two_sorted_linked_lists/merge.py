# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return dummy.next


s = Solution()
def create_linked_list(nums):
    head = ListNode(nums[0])
    node = head
    for n in nums[1:]:
        new_node = ListNode(n)
        node.next = new_node
        node = node.next

    return head
        
def print_linked_list(linked_list: ListNode):
    node = linked_list
    while node:
        print(f"{node.val} -> ")
        node = node.next

def example_1():
    list1 = [1,2,4]
    list2 = [1,3,4]
    a = create_linked_list(list1)
    b = create_linked_list(list2)
    m = s.mergeTwoLists(a, b)
    print_linked_list(m)

example_1()
