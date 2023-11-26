# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next

        nums.sort()

        node = head
        i = 0
        while node:
            node.val = nums[i]
            i += 1
            node = node.next

        return head
        