# Definition for singly-linked list.
# 1, 2, 3, 4, 5
# n = 2
# 0  1  2  3
# 1, 2, 3, 5
#
# 0  1  2  3  4, <-- i
# 1, 2, 3, 4, 5
# 5  4  3  2  1
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            n -= 1
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return head
        

def get_linked_list(nums):
    head = ListNode(nums[0])
    node = head
    for n in nums[1:]:
        newNode = ListNode(n)
        node.next = newNode
        node = newNode
    return head

def print_linked_list(list):
    node = list
    while node:
        print(f"[{node.val}] -> ")
        node = node.next
    print("\n")

s = Solution()

def example_1():
    nums = [1, 2, 3, 4, 5]
    linked_list = get_linked_list(nums)
    correct = get_linked_list([1, 2, 3, 5])
    r = s.removeNthFromEnd(linked_list, 2)
    print_linked_list(correct)
    print_linked_list(r)


def main():
    example_1()
    print("hi")

main()


            
            