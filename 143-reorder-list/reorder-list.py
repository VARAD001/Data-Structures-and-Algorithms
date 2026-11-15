# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        new_head = slow.next
        slow.next = None
        current = new_head
        after = current
        pre = None
        while current:
            after = current.next
            current.next = pre
            pre = current
            current = after
        new_head = pre
        current = head
        while new_head and current:
            after = current.next
            current.next = new_head
            new_head = new_head.next
            current = current.next
            current.next = after
            current = current.next
        return head

        