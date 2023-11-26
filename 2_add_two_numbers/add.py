# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        digit = ListNode(0)
        dummy.next = digit
        carry = False

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            digit.val = a + b
            if carry:
                digit.val += 1

            if digit.val > 9:
                carry = True
                digit.val = digit.val % 10
            else:
                carry = False

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2 or carry:
                new_digit = ListNode(0)
                digit.next = new_digit
                digit = new_digit

        return dummy.next
