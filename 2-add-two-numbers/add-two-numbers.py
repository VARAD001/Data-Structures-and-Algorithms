# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        first = l1
        sec = l2
        while first or sec:
            if not first.next and sec.next:
                first.next = ListNode(0)
            elif not sec.next and first.next:
                sec.next = ListNode(0)
            first = first.next
            sec = sec.next
        carry = 0
        dummy = ListNode(0)
        current = dummy
        first = l1
        sec = l2
        while first:
            carry += (first.val + sec.val)
            current.next = ListNode(carry%10)
            carry //= 10
            current = current.next
            first = first.next
            sec = sec.next
        print(carry)
        if carry:
            current.next = ListNode(carry)
        return dummy.next

        