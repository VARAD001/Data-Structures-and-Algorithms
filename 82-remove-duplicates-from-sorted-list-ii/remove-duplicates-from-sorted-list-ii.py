# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        if not head.val == head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        dupe = head.val
        while head and head.val == dupe:
            head = head.next
        return self.deleteDuplicates(head)
        
        