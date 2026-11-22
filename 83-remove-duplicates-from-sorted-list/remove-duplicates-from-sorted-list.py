# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        if not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            return head.next
        return head





































































































        