# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        current = dummy = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            current.next = ListNode(val%10)
            current = current.next
            carry = val //10
            val //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next