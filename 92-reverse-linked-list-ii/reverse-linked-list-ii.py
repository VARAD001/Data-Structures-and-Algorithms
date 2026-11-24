# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        def reverse_list(head, n):
            if n == 1:
                return head, head.next
            new_head, nextnode = reverse_list(head.next, n-1)
            head.next.next = head
            head.next = nextnode
            return new_head, nextnode
        
        if left == 1:
            new_head, _ = reverse_list(head, right)
            return new_head
        
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
        