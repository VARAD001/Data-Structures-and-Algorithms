# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        return self.rec(head,[n])

    def rec(self, head, n):
        if not head:
            return None
        head.next = self.rec(head.next, n)
        n[0] -= 1
        if n[0] == 0:
            return head.next
        return head
        
        